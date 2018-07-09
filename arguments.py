import config as ITEST_Config

import argparse
import typing

def parse_cmd_line_args(args: typing.List[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
                                    description=f"""{ITEST_Config.Meta.name}, {ITEST_Config.Meta.version}\n
                                                    {ITEST_Config.Meta.description}""", 
                                    epilog=f"Copyright (C) 2018, {ITEST_Config.Meta.author}"
                                    formatter_class=argparse.RawDescriptionHelpFormatter
                                )

    arg_parser.add_argument(
                        "-g", 
                        "--gui", 
                        dest="want_gui", 
                        action="store_true", 
                        default=False, 
                        help=f"run {ITEST_Config.Meta.name} with a graphical user interface"
                    )

    arg_parser.add_argument(
                        "-v", 
                        "--version", 
                        action="version", 
                        version=f"{ITEST_Config.Meta.version}", 
                        help=f"output {ITEST_Config.Meta.name} version string"
                    )

    arg_parser.add_argument(
                        "-l", 
                        "--log-file", 
                        metavar="LOG_FILE", 
                        dest="log_file", 
                        nargs="?", 
                        default=f"{ITEST_Config.Meta.name}.log", 
                        help=f"specify {ITEST_Config.Meta.name} log file"
                    )
    
    arg_parser.add_argument(
                        "-c", 
                        "--configuration-file", 
                        metavar="CONFIGURATION_FILE", 
                        dest="configuration_file", 
                        nargs="?", 
                        default=f"{ITEST_Config.Meta.name}.ini", 
                        help=f"specify {ITEST_Config.Meta.name} configuration file"
                    )

    return arg_parser.parse_intermixed_args()
