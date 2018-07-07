# import variables as ITEST_Variables - ITEST_Arguments.parse()
import meta as ITEST_Meta

import sys
import argparse
import typing

def itest(arguments: typing.List[str]) -> None:
    arg_parser = argparse.ArgumentParser(description=f"{ITEST_Meta.NAME}, version: {ITEST_Meta.VERSION}\n{ITEST_Meta.DESCRIPTION}", epilog=f"Copyright (C) 2018, {ITEST_Meta.AUTHOR}", formatter_class=argparse.RawDescriptionHelpFormatter)

    arg_parser.add_argument("-g", "--gui", dest="want_gui", action="store_true", default=True, help=f"run {ITEST_Meta.NAME} with a graphical user interface (default)")
    arg_parser.add_argument("-c", "--cli", dest="want_cli", action="store_true", default=False, help=f"run {ITEST_Meta.NAME} with a command line interface")

    args: argparse.Namespace = arg_parser.parse_intermixed_args()

    '''
    if args.want_gui:
        ITEST_Ui.gui_run()
    else:
        ITEST_Ui.cli_run()
    '''
        

if __name__ == "__main__":
    itest(sys.argv[1:])
