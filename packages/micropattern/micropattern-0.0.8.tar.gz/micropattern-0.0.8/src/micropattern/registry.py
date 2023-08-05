import json
import os
from contextlib import contextmanager
from typing import Dict
from typing import Optional, ContextManager

import requests

from .utils.logger import Logger


class RegistryConfig:
    def __init__(self, host: str, port: int):
        self.registry_host = host
        self.registry_port = port

    @staticmethod
    def from_env():
        host = os.environ.get('MP_REGISTRY_HOST', None)
        port = int(os.environ.get('MP_REGISTRY_PORT', -1))
        if not host or port < 0:
            raise ValueError("Please set registry host and port in environment variable")
        return RegistryConfig(host=host, port=port)


class Registry(object):
    def __init__(self, key, default_values: Optional[Dict] = None, config: Optional[RegistryConfig] = None):
        self.__data: Optional[Dict] = None
        if not key:
            raise ValueError("Need specify key of registry")
        self.__default_values = default_values
        self.__key = key
        self.__registry_config = config if config else RegistryConfig.from_env()
        self.__is_loaded = False
        self.__logger = Logger(f'{key}_registry')

    def __load_remote_configs(self):
        self.__is_loaded = False
        try:
            remote_config_url = f"http://{self.__registry_config.registry_host}:{self.__registry_config.registry_port}/get?key={self.__key}"
            response = requests.get(remote_config_url, timeout=3)
            self.__data = response.json()
            self.__is_loaded = True
        except Exception as e:
            self.__logger.error(f"Load remote configs failed: {str(e)}")
            self.__data = self.__default_values
        return self

    def __save_configs(self):
        try:
            endpoint = f"http://{self.__registry_config.registry_host}:{self.__registry_config.registry_port}/update"
            payload = {
                "key": self.__key,
                "value": json.dumps(self.__data)
            }
            response = requests.post(endpoint, json=payload)
            if response.status_code != 200:
                raise RuntimeError(f'Could not save registry values: [{response.status_code}] [{response.content.decode("utf-8")}]')
            data = response.json()
            if not data.get('success', False):
                raise RuntimeError(f'Could not save registry values: [{data}]')
        except Exception as e:
            self.__logger.error(f"Save remote configs failed: {str(e)}")
        return self

    def __getattribute__(self, item: str):
        if item.startswith('_Registry__'):
            return super(Registry, self).__getattribute__(item)
        if self.__data is None and not self.__is_loaded:
            self.__load_remote_configs()
        if item in self.__data:
            return self.__data[item]
        return super(Registry, self).__getattribute__(item)

    @contextmanager
    def __call__(self, *args, **kwargs) -> ContextManager["Registry"]:
        try:
            if self.__data is None and not self.__is_loaded:
                self.__load_remote_configs()
            yield self
        finally:
            self.__save_configs()

    def __setattr__(self, key, value):
        if key.startswith('_Registry__'):
            super(Registry, self).__setattr__(key, value)
        if self.__data and key in self.__data:
            self.__data[key] = value
        else:
            super(Registry, self).__setattr__(key, value)
