import config as ITEST_Config

import tkinter
import tkinter.font
import typing

# font, text colour (red and normal)

# colour: #000000.#FFFFFF
# .config(background=bg_color, fg=foreground_color)
# must do explicit import tkinter.font

def _font_handling():
    custom_font: tkinter.font.Font = tkinter.font.Font(ITEST_Config.gui.font_family, ITEST_Config.gui.font_size, ITEST_Config.gui.font_weight)

    # text_widget.highlight_pattern("pattern", "TAG_NAME")
    text_widget.tag_configure("TAG_NAME", foreground=ITEST_Config.gui.font_colour, font=custom_font)
    text_widget.tag_add("TAG_NAME", "start", "end")

def run_gui() -> None:
    CONSOLE_TITLE: str = f'''{ITEST_Config.meta.name} Console 
                        ({'DEBUG' if __debug__ else 'RELEASE'}) - {ITEST_Config.meta.version}'''
    console_window: tkinter.Tk = _create_console_window(CONSOLE_TITLE)

    VIEWER_TITLE: str = f'''{ITEST_Config.meta.name} Viewer 
                        ({'DEBUG' if __debug__ else 'RELEASE'}) - {ITEST_Config.meta.version}'''
    viewer_window: tkinter.Toplevel = _create_viewer_window(console_window, VIEWER_TITLE)

    _center_windows(console_window, viewer_window)

    # NOTE(Ryan): may not need as we focus entry widget 
    console_window.focus_force() 

    tkinter.after(0, ITEST_Config.reload_if_changed())
    tkinter.mainloop()  

def _create_console_window(window_title: str) -> tkinter.Tk:
    console_window: tkinter.Tk = tkinter.Tk()
    console_window.title(window_title)

    console_window_layout_frame = _create_console_window_layout_frame(console_window)

    console_window_text: tkinter.Text = tkinter.Text(master=console_window_layout_frame, wrap="word")
    console_window_text.config(state="disabled")
    console_window_text.grid(row=0, column=0, rowspan=5, columnspan=6, sticky="nsew")
    console_window_text_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(master=console_window_layout_frame)
    console_window_text.configure(yscrollcommand=console_window_text_scrollbar.set)
    console_window_text_scrollbar.config(command=console_window_text.yview)
    console_window_text_scrollbar.grid(row=0, rowspan=5, column=6, sticky="nsw")

    ITEST_Logging.initialize_gui_logger(console_window_text)

    console_window_command_entry: tkinter.Entry = tkinter.Entry(master=console_window_layout_frame)
    console_window_command_entry.grid(row=6, column=0, columnspan=5, sticky="we", ipady="2", ipadx="2")
    console_window_command_entry.focus_set()

    command_interpreter: ITEST_UI.GUICommandInterpreter = ITEST_UI.create_gui_command_interpreter()

    process_command: typing.Callable[[tkinter.Event], None] = lambda event: command_interpreter.process_command() 
    console_window_command_entry.bind("<Return>", process_command)

    console_window_command_entry_button: tkinter.Button = tkinter.Button(master=console_window_frame, text="Enter")
    console_window_command_entry_button.bind("<Button-1>", process_command)
    console_window_command_entry_button.grid(row=6, column=5, columnspan=2, sticky="we")


    return console_window

def _create_console_window_layout_frame(console_window: tkinter.Tk) -> tkinter.Frame:
    console_window.grid_rowconfigure(0, weight=1)
    console_window.grid_columnconfigure(0, weight=1)

    console_window_layout_frame: tkinter.Frame = tkinter.Frame(master=console_window, padx=12, pady=12)
    console_window_layout_frame.grid(column=0, row=0, sticky="nsew")

    '''
    +---+---+---+---+---+---+---+---+
    |   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
    +---+---+---+---+---+---+---+---+
    | 0 |                       | S |
    +---+   TEXT                + C +
    | 1 |                       | R |
    +---+                       + O +
    | 2 |                       | L |
    +---+                       + L +
    | 3 |                       |   |
    +---+                       +   +
    | 4 |                       |   |
    +---+---+---+---+---+---+---+---+
    | 5 |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+
    | 6 |   ENTRY           | BTN   |
    +---+---+---+---+---+---+---+---+
    '''

    console_window_layout_frame.grid_columnconfigure(0, weight=10)
    console_window_layout_frame.grid_columnconfigure(1, weight=10)
    console_window_layout_frame.grid_columnconfigure(2, weight=10)
    console_window_layout_frame.grid_columnconfigure(3, weight=10)
    console_window_layout_frame.grid_columnconfigure(4, weight=10)
    console_window_layout_frame.grid_columnconfigure(5, weight=10)
    console_window_layout_frame.grid_columnconfigure(6, weight=1)
    console_window_layout_frame.grid_rowconfigure(0, weight=10)
    console_window_layout_frame.grid_rowconfigure(1, weight=10)
    console_window_layout_frame.grid_rowconfigure(2, weight=10)
    console_window_layout_frame.grid_rowconfigure(3, weight=10)
    console_window_layout_frame.grid_rowconfigure(4, weight=10)
    console_window_layout_frame.grid_rowconfigure(5, weight=1)
    console_window_layout_frame.grid_rowconfigure(6, weight=10)

    return console_window_layout_frame


def _create_viewer_window(console_window: tkinter.Tk, window_title: str) -> tkinter.Toplevel:


def _center_windows(window1: tkinter.Tk, window2: tkinter.Toplevel) -> None:
    SCREEN_WIDTH: int = window_root.winfo_screenwidth()
    SCREEN_HEIGHT: int = window_root.winfo_screenheight()

    WINDOW_TOTAL_WIDTH: int = WINDOW_CONSOLE_WIDTH + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH
    WINDOW_CONSOLE_X: int = int((SCREEN_WIDTH / 2) - ((WINDOW_TOTAL_WIDTH) / 2))
    WINDOW_CONSOLE_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_CONSOLE_HEIGHT) / 2))
    window_console.geometry(f"{WINDOW_CONSOLE_WIDTH}x{WINDOW_CONSOLE_HEIGHT}+{WINDOW_CONSOLE_X}+{WINDOW_CONSOLE_Y}")



    WINDOW_VIEWER_X: int = WINDOW_CONSOLE_X + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH
    WINDOW_VIEWER_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_VIEWER_HEIGHT) / 2))
    window_viewer: tkinter.Toplevel = tkinter.Toplevel(window_console)
    window_viewer.title(WINDOW_VIEWER_TITLE)
    window_viewer.geometry(f"{WINDOW_VIEWER_WIDTH}x{WINDOW_VIEWER_HEIGHT}+{WINDOW_VIEWER_X}+{WINDOW_VIEWER_Y}")
    # tkinter.PhotoImage

    window_console.focus_force()
    window_root.mainloop() 

if __name__ == "__main__":
    run()
