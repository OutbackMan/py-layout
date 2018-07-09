import config as ITEST_Config
import logging as ITEST_Logging

import cmd
import os
import tkinter

class Commands():
    def __init__(self):
        self.intro = f"Welcome to {ITEST_Config.meta.name}. Type help or ? to list commands\n"
        self.prompt = f"({ITEST_Config.meta.name})"

    def preloop(self):
        self._local_variables = {}
        self._global_variables = {}

    def postloop(self):
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

class CLICommandPrompt(cmd.Cmd, Commands):
    def __init__(self):
        super().__init__(self) # cooperative super()

class GUICommandPrompt(cmd.Cmd, Commands):
    def __init__(self, input_widget: tkinter.Entry, output_widget: tkinter.Text):
        super().__init__(self, stdin=input_widget, stdout=output_widget)
        self.use_rawinput = False

x = CLICommandPrompt()
x.cmdloop()
