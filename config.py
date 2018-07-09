import configparser
import typing
import dataclasses

@dataclasses.dataclass(frozen=True)
class Meta:
    name: str = "ITest"
    version: str = "v0.0.1"
    description: str = "Some description"
    author: str = "Ryan McClue"
    
@dataclasses.dataclass
class GUI:
    pass

_dataclasses: typing.List[typing.Type[typing.Any]] = [Meta(), GUI()]

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

