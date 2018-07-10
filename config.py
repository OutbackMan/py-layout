import configparser
import typing
import dataclasses

@dataclasses.dataclass(frozen=True)
class Meta:
    name: str = "ITest"
    version: str = "v0.0.1"
    description: str = "Some description"
    author: str = "Ryan McClue"

meta: Meta = Meta()

@dataclasses.dataclass
class Logging:
    log_file: str = f"{meta.name.lower()}.log"
    debug_msg_format: str = '''[%(name)s:%(levelname)s] (%(asctime)s) - 
                                %(filename)s:%(funcName)s():%(lineno)s "%(message)s"'''
    debug_date_format: str = "%d/%m/%Y, %H:%M:%S"
    release_msg_format: str = "%(message)s"
    release_date_format: str = "%d/%m/%Y, %H:%M:%S"

logging: Logging = Logging()

@dataclasses.dataclass
class GUI:
    bg_color: str = "#123123"
    fg_color: str = "#123123"
    font: str = ""
    font_color: str = "#123123"

gui: Gui = Gui()

_ConfigDataclass: typing.TypeVar = typing.TypeVar("ConfigDataclass", Logging, GUI)
_dataclasses: typing.List[_ConfigDataclass] = [logging, gui]

def reload_if_changed() -> None:
    if os.path.exists("itest.ini"):
        if not hasattr(reload_if_changed, "config_file_mod_time") or os.stat("itest.ini").st_mtime != reload_if_changed.config_file_mod_time:
            _reload_config()
            reload_if_change.config_file_mod_time = os.stat("itest.ini").st_mtime

def _reload_config() -> None:
    config = configparse.ConfigParser()
    config.read("itest.ini")

    for config_dataclass_name in config.sections():
        if _is_valid_dataclass_name(config_dataclass_name):
            for config_dataclass_variable_name, config_dataclass_variable_value in config.items(config_dataclass_name):
                if _is_valid_dataclass_variable_name(config_dataclass_name, config_dataclass_variable_name):
                    dataclass_variable_value = getattr(config_dataclass_name, config_dataclass_variable_name)
                    if isinstance(dataclass_variable_value, int):
                        setattr(dataclass_name, config_dataclass_variable_name, int(config_dataclass_variable_value))

def _is_valid_dataclass_name(dataclass_name: str) -> bool:
    for config_dataclass in config_dataclasses:
        return dataclass_name == config_dataclass.__class__.__name__
     
def _is_valid_dataclass_variable_name(config_dataclass_name: str, dataclass_variable_name: str) -> bool:
    for config_dataclass_variable_name in vars(config_dataclass_name):
        if dataclass_variable_name == available_dataclass_variable_name:

