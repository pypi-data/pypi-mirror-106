from contextlib import contextmanager
from typing import Optional, Union, ContextManager

import pika
from pika import ConnectionParameters

from .logger import Logger


class _BasicPublisher:
    def __init__(self, logger, queue_name, channel):
        self.queue_name = queue_name
        self.channel = channel
        self.__logger = logger

    def enqueue(self, message: Union[bytes, str]):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message if isinstance(message, bytes) else message.encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        if self.__logger:
            self.__logger.info(f"Enqueued message, size={len(message) / 1024}KB")


class BasicPublish:
    def __init__(self, host: str, port: int, username: str, password: str, queue_name: str, debug: bool = False):
        self.connection: Optional[pika.BlockingConnection] = None
        self.channel = None
        self.conn_params = {
            "host": host,
            "port": port,
            "username": username,
            "password": password
        }
        self.queue_name = queue_name
        self.__is_connected = False
        self.__debug = debug
        self.__logger: Optional[Logger] = Logger(f"{queue_name}_queue") if debug else None

    @contextmanager
    def __call__(self, *args, **kwargs) -> ContextManager["_BasicPublisher"]:
        try:
            if not self.__is_connected:
                self.connect()
            yield _BasicPublisher(self.__logger, self.queue_name, self.channel)
        except Exception as e:
            if self.__debug:
                self.__logger.error(str(e))
            raise
        finally:
            self.disconnect()

    def connect(self):
        self.__setup_queue(ConnectionParameters(
            host=self.conn_params.get("host"),
            port=self.conn_params.get("port"),
            credentials=pika.PlainCredentials(
                username=self.conn_params.get("username"),
                password=self.conn_params.get("password")
            )
        ))
        self.__is_connected = True
        if self.__debug:
            self.__logger.info(f"Connected to RabbitMQ server")
        return self

    def disconnect(self):
        if not self.__is_connected:
            return
        self.__is_connected = False
        if self.connection:
            self.connection.close()
        if self.__debug:
            self.__logger.info(f"Disconnected from RabbitMQ server")

    def __setup_queue(self, params: ConnectionParameters):
        conn = pika.BlockingConnection(params)
        channel = conn.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)
        # channel.exchange_declare(exchange=self.topic, exchange_type='topic')
        self.channel = channel
        self.connection = conn

    @property
    def is_connected(self):
        return self.__is_connected
