import config as ITEST_Config
import ui as ITEST_UI

import sys
import argparse
import typing

def _parse_cmd_line_args(args: typing.List[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(description=f"{ITEST_Meta.NAME}, {ITEST_Meta.VERSION}\n{ITEST_Meta.DESCRIPTION}", epilog=f"Copyright (C) 2018, {ITEST_Meta.AUTHOR}", formatter_class=argparse.RawDescriptionHelpFormatter)

    arg_parser.add_argument("-g", "--gui", dest="want_gui", action="store_true", default=True, help=f"run {ITEST_Meta.NAME} with a graphical user interface (default)")
    arg_parser.add_argument("-c", "--cli", dest="want_cli", action="store_true", default=False, help=f"run {ITEST_Meta.NAME} with a command line interface")

    return arg_parser.parse_intermixed_args()

def itest() -> None:
    ITEST_Config.initialize()

    cmd_line_args: argparse.Namespace = _parse_cmd_line_args(sys.argv[1:])

    if cmd_line_args.want_gui:
        ITEST_UI.run_gui()
    else:
        ITEST_UI.run_cli()

if __name__ == "__main__":
  itest()



import cmd

class CommandPrompt(cmd.Cmd):
    def __init__(self, stdin, stdout, want_gui):
        super.__init__(self)
        intro = "Welcome to asdasd. Type help or ? to list commands\n"
        prompt = "(asdasd)"
        if (want_gui):
            self.use_rawinput = False
    def do_command(self, args):
        "This text will be printed on help"
        pass

    def do_help(self, args):
        pass

    def do_EOF(self, args):
        return True



