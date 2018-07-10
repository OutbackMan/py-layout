import config as ITEST_Config

import logging
import typing
import tkinter

logger: logging.Logger = logging.getLogger(ITEST_Config.meta.name)

if __debug__:
    _add_debug_logger_settings(logger)
else:
    _add_release_logger_settings(logger)

def initialize_gui_logger(log_widget: tkinter.Text):
    global logger

    logger.setHandler(_GuiLoggerHandler(log_widget))
    
def initialize_cli_logger():
    global logger

def _add_debug_logger_settings():
    logger.setLevel(logging.DEBUG)

def _add_release_logger_settings():
    logger.addFilter(_ReleaseLoggerFilter())

    file_handler = logging.FileHandler(ITEST_Config.logging.log_file)
    file_handler_formatter = logging.Formatter(ITEST_Config.logging.release_msg_format)
    file_handler.setFormatter(file_handler_formatter)
    file_handler.setLevel(logging.CRITICAL)
    logger.addHandler(file_handler)


def initialize_debug(output_stream: typing.Union[typing.TextIO, tkinter.Text], log_file: str): 
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
