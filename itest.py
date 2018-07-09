import config as ITEST_Config
import arguments as ITEST_Arguments
import ui as ITEST_UI

import sys
import typing

def itest() -> None:
    cmd_line_args: argparse.Namespace = ITEST_Arguments.parse_cmd_line_args(sys.argv[1:])

    if cmd_line_args.want_gui:
        ITEST_UI.run_gui()
    else:
        ITEST_UI.run_cli()

if __name__ == "__main__":
  itest()



