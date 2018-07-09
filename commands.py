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



