import config-variables as ITEST_ConfigVariables

import sys
import argparse
import typing
import os


def itest(config_variables_file: str, arguments: typing.List[str]) -> None:
    prev_config_variables_file_mod_time = ITEST_ConfigVariables.initialize(config_variables_file)

    arg_parser = argparse.ArgumentParser(description=f"{ITEST_Meta.NAME}, version: {ITEST_Meta.VERSION}\n{ITEST_Meta.DESCRIPTION}", epilog=f"Copyright (C) 2018, {ITEST_Meta.AUTHOR}", formatter_class=argparse.RawDescriptionHelpFormatter)

    arg_parser.add_argument("-g", "--gui", dest="want_gui", action="store_true", default=True, help=f"run {ITEST_Meta.NAME} with a graphical user interface (default)")
    arg_parser.add_argument("-c", "--cli", dest="want_cli", action="store_true", default=False, help=f"run {ITEST_Meta.NAME} with a command line interface")

    args: argparse.Namespace = arg_parser.parse_intermixed_args()

    while True:
        cur_config_variables_file_mod_time = os.stat(config_variables_file).st_mtime
        if cur_config_variables_file_mod_time != prev_config_variables_file_mod_time:
            ITEST_ConfigVariables.reload(config_variables_file)
            prev_config_variables_file_mod_time = cur_config_variables_file_mod_time 

        if args.want_gui:
            import gui as ITEST_GUI
            ITEST_GUI.run()
        else:
            import cli as ITEST_CLI
            ITEST_CLI.run()


if __name__ == "__main__":
  CONFIG_FILE: str = "config.variables"

  itest(CONFIG_FILE, sys.argv[1:])
