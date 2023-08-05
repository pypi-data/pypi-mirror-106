import logging

FILE_LOG_ENABLED = False
FILE_LOG_PATH = ''

DEBUG = logging.DEBUG


class Logger:
    def __init__(self, module_name, logging_level=logging.INFO):
        self.__logger = logging.getLogger('xcrawler')
        self.__logging_level = logging_level
        self.__module_name = module_name
        if len(self.__logger.handlers) == 0:
            if FILE_LOG_ENABLED:
                # File handler
                handler = logging.FileHandler(FILE_LOG_PATH)
                handler.setLevel(logging.DEBUG)
                handler.setFormatter(logging.Formatter(f'[%(asctime)s][%(levelname)s]%(message)s'))
                self.__logger.addHandler(handler)
            # Stream handler
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(logging.Formatter(f'%(message)s'))
            self.__logger.addHandler(handler)

            self.__logger.propagate = False
            self.__logger.setLevel(logging.DEBUG)

    # std flush
    def flush(self):
        pass

    # std log
    def write(self, buf):
        self.__logger.log(self.__logging_level, f'[{self.__module_name}] {buf.rstrip()}')

    def info(self, msg):
        self.__logger.info(f'[{self.__module_name}] {msg}')

    def error(self, msg):
        self.__logger.error(f'[{self.__module_name}] {msg}')
