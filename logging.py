import config as ITEST_Config

import logging
import typing
import tkinter

def initialize(output_stream: typing.Union[typing.TextIO, tkinter.Text], log_file: str): 
    logger: logging.Logger = logging.getLogger(f"{ITEST_Config.Meta.name}")

    if __debug__:
        logger.setLevel(logging.DEBUG)

        ALL_LEVELS_MSG_FORMAT_STR: str = '''[%(name)s:%(levelname)s] (%(asctime)s) - 
                                %(filename)s:%(funcName)s():%(lineno)s "%(message)s"'''
        DATE_FORMAT_STR: str = "%d/%m/%Y, %H:%M:%S"
    else:
        logger.addFilter(_ReleaseLoggerFilter())

        critical_level_file_handler = logging.FileHandler(log_file)
        critical_level_formatter = logging.Formatter("")
        critical_level_file_handler.setFormatter(critical_level_formatter)
        critical_level_file_handler.setLevel(logging.CRITICAL)
        logger.addHandler(critical_level_file_handler)

        
        if isinstance(output_stream: tkinter.Text):
            logger.addHandler(_GuiLoggerHandler(output_stream))

        INFO_LEVEL_MSG_FORMAT_STR: str = "[%(name)s:%(levelname)s] \"%(message)s\""

        CRITICAL_LEVEL_MSG_FORMAT_STR: str = '''[%(name)s:%(levelname)s] (%(asctime)s) - 
                                %(filename)s:%(funcName)s():%(lineno)s "%(message)s"'''
        CRITICAL_LEVEL_DATE_FORMAT_STR: str = "%d/%m/%Y, %H:%M:%S"

        # logger_file_handler.setFormatter(logging.CRITICAL) // want date and such
        logger.addHandler(logger_file_handler)

    

class _ReleaseLoggerFilter(logging.Filter):
    def __init__(self):
        super().__init__(self)
    def filter(self, log_record):
        return log_record.levelno in (logging.INFO, logging.CRITICAL)

class _GuiLoggerHandler(logging.StreamHandler):
    def __init__(self, output_text_widget: tkinter.Text)
        super().__init__(self)
        self.output_text_widget = output_text_widget
    def emit(self, log_record):
        msg: str = self.format(log_record)
        self.output_text_widget.insert("end", msg + "\n")
        self.flush()

if __debug__:
    logging.basicConfig(level=logging.DEBUG, format=_LOGGER_MSG_FORMAT_STR, datefmt=_LOGGER_DATE_FORMAT_STR)
else:
    logging.basicConfig(filename="itest.log", level=logging.ERROR, format=_LOGGER_MSG_FORMAT_STR, datefmt=_LOGGER_DATE_FORMAT_STR)

logger = logging.getLogger()
