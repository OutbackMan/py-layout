import config as ITEST_Config
import logging as ITEST_Logging

import cmd
import os
import tkinter

def initialize_cli_command_interpreter() -> CLICommandInterpreter:
    return CLICommandInterpreter()

def initialize_gui_command_interpreter(gui_stdin: GUIStdin, gui_stdout: GUIStdout) -> GUICommandInterpreter:
    return GUICommandInterpreter(gui_stdin, gui_stdout)

class Commands():
    def __init__(self):
        self._local_variables = {}
        self._global_variables = {}
        self.intro = f"Welcome to {ITEST_Config.meta.name}. Type help or ? to list commands\n"

    def on_exit(self):
        # print exiting...

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        # return true if want to quit
        return stop

    def do_help(self, args):
        '''we just want this docstring '''
        super().do_help(self, args)

    def do_shell(self, args):
        ''' when line begins with !'''
        os.system(args)

    def default(self, line):
        ''' execute python code '''
        try:
            exec(line, self._local_variables, self._global_variables) 
        except:
           # print info  
    
    def do_hist(self, line):
        # print self._command_history

    def do_command(self, args):
        '''Perform some operation: COMMAND ARG1 ARG2'''
        pass

    def complete_command(self, text, line, begidx, endidx):
        return [i for i in parameter_options if i.startswith(text)] 

    def do_exit(self, args):
        # return some notifier

    def emptyline(self):
        pass

    def do_EOF(self, args):
        return True

class CLICommandInterpreter(cmd.Cmd, Commands):
    def __init__(self):
        super().__init__(self)

    # TODO(Ryan)
    def process_command(self):
        pass

class GUICommandInterpreter(cmd.Cmd, Commands):
    def __init__(self, stdin: GUIStdin, stdout: GUIStdout):
        super().__init__(self, stdin=stdin, stdout=stdout)

        self.stdout.write(f"{self.intro}\n")
        self.stdout.flush()

    def process_command(self):
        line: str = self.stdin.readline()
        if not len(line):
            line = "EOF"
        else:
            line = line.rstrip("\r\n")
        line = self.precmd(line)
        self.onecmd(line)
        self.postcmd(False, line)

class GUIStdin():
    def __init__(self, input_widget: tkinter.Entry):
        self.input_widget = input_widget

    def readline() -> str:
        line: str = self.input_widget.get() 
        self.input_widget.delete(0, "end")
        return line

class GUIStdout():
    def __init__(self, output_widget: tkinter.Text):
        self.output_widget = output_widget

    def write(text: str) -> None:
        self.output_widget.config(state="normal")
        self.output_widget.insert("end", f"{text}\n")
        self.output_widget.see("end")

    def flush() -> None:
        self.output_widget.config(state="disabled")
