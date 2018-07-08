# import logger as ITEST_Logger

import typing
import dataclasses
import shlex
import os

@dataclasses.dataclass(frozen=True)
class Meta:
    name: str = "ITest"
    version: str = "v0.0.1"
    description: str = "Some description"
    author: str = "Ryan McClue"

@dataclasses.dataclass
class Audio:
    value: int = 1,
    value2: bool = False


audio: Audio
misc: Misc

@dataclass
class ValueHolder:
    # struct type --> type: typing.TypeVar
    # struct

holders: typing.List[ValueHolder]

def add_value_holder(holder: Any):
    holders.push(ValueHolder(type(holder), holder)



def init(config_variables_file_name: str) -> None:
    add_value_holder(audio)
    add_value_holder(misc)

    reload_variables()

    return os.stat(config_variables_file).st_mtime

def reload_variables():
    if os.path.exists(config_variables_file_name):
        config_variables_file_data: str = None
        try:
            config_variables_file: typing.TextIO = open(config_variables_file_name)
            config_variables_file_data: str = config_variables_file.read()
            config_variables_file.close()
        except IOError:
            ITEST_Logger.logger.exception("I/O exception encountered reading config variables file")

        current_holder: ValueHolder = None

        line_number: int = 1

        line: str
        for line in config_variables_file_data:
            stripped_line: str = line.strip()
            if stripped_line[0] == ":":
                if len(stripped_line) < 2:
                    ITEST_Logger.logger.error(f"(Line: {line_number}) Line starting with ':' must have '/' and a name after it")
                else:
                    if stripped_line[1] != "/":
                        ITEST_Logger.logger.error(f"(Line: {line_number}) Expected a '/' after ':'")
                    else:
                        folder_name: str = stripped_line[2:]
                        found_folder: bool = False

                        for holder in holders:
                            if holder.__class__.__name__ == folder_name:
                                current_holder = holder
                                found_folder = True

                        if !found_folder:
                            # error log
            elif stripped_line[0] == "#":
                continue 
            else:
                if " " in stripped_line:
                    if current_holder == None:
                        ITEST_Logger.logger.error(f"(Line: {line_number}) Variables must proceed after directory name")
                    else:
                        variable_name: str, variable_value: str = shlex.split(stripped_line)
                        found_holder_item: bool = False
                        for holder_item_name in vars(current_holder):
                            if variable_name == holder_item_name:
                                found_holder_item = True
                                break

                        if !found_holder_item:
                            #error
                        else:
                            poke_value(current_holder, variable_name, variable_value, line_number)
                else:
                    ITEST_Logger.logger.error(f"(Line: {line_number}) Expected a space after variable name")

            line_number += 1
    else:
        ITEST_Logger.logger.error(f"Config variables file: {config_variables_file_name} does not exist")


def poke_value(current_holder: Holder, variable_name: str, variable_value: str, line_number: int) -> None:
    holder_variable = getattr(current_holder, variable_name)

    if isinstance(holder_variable, int):
        setattr(current_holder, variable_name, int(variable_value)) 
    elif isinstance(holder_variable, float):
        setattr(current_holder, variable_name, float(variable_value)) 
    elif isinstance(holder_variable, str):
        setattr(current_holder, variable_name, str(variable_value))
    elif isinstance(holder_variable, bool):
        setattr(current_holder, variable_name, bool(variable_value)) 
    else:
        # ERROR(Ryan): 

