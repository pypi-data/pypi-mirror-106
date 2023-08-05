from ..registry import Registry


class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def postgre_connection_string(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


class RawDataDatabaseConfig(Registry, DatabaseConfig):
    def __init__(self):
        Registry.__init__(self, 'data_db')
        DatabaseConfig.__init__(self)


class MQConfig(Registry):
    host: str
    port: int
    user: str
    password: str

    def __init__(self):
        Registry.__init__(self, 'message_queue')
