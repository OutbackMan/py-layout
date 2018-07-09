import config as ITEST_Config

import logging
import typing # typing.Union[int, str]

def initialize(): 
    logger = logging.getLogger(f"{ITEST_Config.Meta.name}")

    if __debug__:

    # debug --> critical to log file

    


_LOGGER_MSG_FORMAT_STR: str = "[%(name)s:%(levelname)s] (%(asctime)s) - %(filename)s:%(funcName)s():%(lineno)s \"%(message)s\""
_LOGGER_DATE_FORMAT_STR: str = "%d/%m/%Y, %H:%M:%S"

if __debug__:
    logging.basicConfig(level=logging.DEBUG, format=_LOGGER_MSG_FORMAT_STR, datefmt=_LOGGER_DATE_FORMAT_STR)
else:
    logging.basicConfig(filename="itest.log", level=logging.ERROR, format=_LOGGER_MSG_FORMAT_STR, datefmt=_LOGGER_DATE_FORMAT_STR)

logger = logging.getLogger()
