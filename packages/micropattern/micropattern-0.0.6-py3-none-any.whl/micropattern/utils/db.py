from contextlib import contextmanager
from typing import TYPE_CHECKING, ContextManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .logger import Logger

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class Database:
    __SESSION__ = None

    def __init__(self, connection_string: str, name='default', debug=False):
        self.connection_string = connection_string
        self.logger = Logger(f'{name}_db')
        self.debug = debug

    def init_db(self, base):
        # Create engine
        engine = create_engine(self.connection_string, echo=False, poolclass=NullPool)
        # Create meta
        base.metadata.create_all(engine)
        # Session maker
        self.__SESSION__ = sessionmaker(bind=engine)

    @contextmanager
    def __call__(self, *args, **kwargs) -> ContextManager["Session"]:
        session: "Session" = self.__SESSION__()
        try:
            yield session
            session.commit()
            if self.debug:
                self.logger.info("Committed to db")
        except Exception as e:
            session.rollback()
            self.logger.error(str(e))
            raise e
        finally:
            session.close()
