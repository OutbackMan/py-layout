import config as ITEST_Config

import logging
import typing
import tkinter
import tkinter.font

class Logger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(self, name)

        if __debug__:
            super().setLevel(self, logging.DEBUG)
        else:
            super().addFilter(_ReleaseLoggerFilter())
            super().addHandler(_ReleaseLoggerFileHandler())

class _ReleaseLoggerFilter(logging.Filter):
    def __init__(self):
        super().__init__(self)
    def filter(self, log_record):
        return log_record.levelno in (logging.INFO, logging.WARNING, logging.CRITICAL)

class _ReleaseLoggerFileHandler(logging.FileHandler):
    def __init__(self, file_name: str):
        super().__init__(self, file_name)
        super().setFormatter(logging.Formatter(ITEST_Config.logging.release_msg_format))
        super().setLevel(logging.CRITICAL)


class GUILogger(Logger):
    def __init__(self, name: str, output_widget: tkinter.Text):
        super().__init__(self, name)
        super().addHandler(_GUILoggerHandler(output_widget))


class _GuiLoggerHandler(logging.StreamHandler):
    def __init__(self, output_text_widget: tkinter.Text)
        super().__init__(self)
        self.output_text_widget = output_text_widget
        self.font: tkinter.font.Font = tkinter.font.Font(ITEST_Config.gui.font_family, ITEST_Config.gui.font_size, ITEST_Config.gui.font_weight)

        self.output_text_widget.tag_configure("DEBUG", foreground=ITEST_Config.logger.debug_level_font_color, font=self.font)
        self.output_text_widget.tag_configure("INFO", foreground=ITEST_Config.logger.info_level_font_color, font=self.font)
        self.output_text_widget.tag_configure("WARNING", foreground=ITEST_Config.logger.warning_level_font_color, font=self.font)
        self.output_text_widget.tag_configure("ERROR", foreground=ITEST_Config.logger.error_level_font_color, font=self.font)
        self.output_text_widget.tag_configure("CRITICAL", foreground=ITEST_Config.logger.critical_level_font_color, font=self.font)

    def emit(self, log_record):
        msg: str = self.format(log_record)
        msg_tag: str = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"][int(log_record.levelno / 10)]
        self.output_text_widget.config(state="normal")
        self.output_text_widget.insert("end", f"{msg}\n", msg_tag)
        self.output_text_widget.see("end")
        self.output_text_widget.config(state="disabled")
        self.flush()



