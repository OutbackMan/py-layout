import config as ITEST_Config

import tkinter
import typing

# font, text colour (red and normal)

# colour: #000000.#FFFFFF
# .config(background=bg_color, fg=foreground_color)
# must do explicit import tkinter.font

def run_gui() -> None:
    CONSOLE_TITLE: str = f'''{ITEST_ConfigVariables.META.name} Console 
                        ({'DEBUG' if __debug__ else 'RELEASE'}) - {ITEST_ConfigVariables.META.version}'''
    console_window: tkinter.Tk = _create_console_window(CONSOLE_TITLE)

    VIEWER_TITLE: str = f'''{ITEST_ConfigVariables.META.name} Viewer 
                        ({'DEBUG' if __debug__ else 'RELEASE'}) - {ITEST_ConfigVariables.META.version}'''
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

    ITEST_Logging.initialize_gui_logger(text_widget)

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
    +---+   OUTPUT              + C +
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
    | 6 |   INPUT           | ENTER |
    +---+---+---+---+---+---+---+---+
    '''

    console_window_frame.grid_columnconfigure(0, weight=10)
    console_window_frame.grid_columnconfigure(1, weight=10)
    console_window_frame.grid_columnconfigure(2, weight=10)
    console_window_frame.grid_columnconfigure(3, weight=10)
    console_window_frame.grid_columnconfigure(4, weight=10)
    console_window_frame.grid_columnconfigure(5, weight=10)
    console_window_frame.grid_columnconfigure(6, weight=1)
    console_window_frame.grid_rowconfigure(0, weight=10)
    console_window_frame.grid_rowconfigure(1, weight=10)
    console_window_frame.grid_rowconfigure(2, weight=10)
    console_window_frame.grid_rowconfigure(3, weight=10)
    console_window_frame.grid_rowconfigure(4, weight=10)
    console_window_frame.grid_rowconfigure(5, weight=1)
    console_window_frame.grid_rowconfigure(6, weight=10)

    return console_window_frame_layout


def _create_viewer_window(console_window: tkinter.Tk, window_title: str) -> tkinter.Toplevel:


def _center_windows(window1: tkinter.Tk, window2: tkinter.Toplevel) -> None:
    SCREEN_WIDTH: int = window_root.winfo_screenwidth()
    SCREEN_HEIGHT: int = window_root.winfo_screenheight()

    WINDOW_TOTAL_WIDTH: int = WINDOW_CONSOLE_WIDTH + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH
    WINDOW_CONSOLE_X: int = int((SCREEN_WIDTH / 2) - ((WINDOW_TOTAL_WIDTH) / 2))
    WINDOW_CONSOLE_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_CONSOLE_HEIGHT) / 2))
    window_console.geometry(f"{WINDOW_CONSOLE_WIDTH}x{WINDOW_CONSOLE_HEIGHT}+{WINDOW_CONSOLE_X}+{WINDOW_CONSOLE_Y}")


    window_console_text: tkinter.Text = tkinter.Text(master=window_console_frame, wrap="word")
    window_console_text.insert("end", "Hello there!\n")
    window_console_text.config(state="disabled")
    window_console_text.grid(row=0, column=0, rowspan=5, columnspan=6, sticky="nsew")
    window_console_text_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(master=window_console_frame)
    window_console_text.configure(yscrollcommand=window_console_text_scrollbar.set)
    window_console_text_scrollbar.config(command=window_console_text.yview)
    window_console_text_scrollbar.grid(row=0, rowspan=5, column=6, sticky="nsw")

    window_console_command_entry: tkinter.Entry = tkinter.Entry(master=window_console_frame)
    window_console_command_entry.grid(row=6, column=0, columnspan=5, sticky="we", ipady="2", ipadx="2")
    window_console_command_entry.focus_set()

    process_command: typing.Callable[[tkinter.Event], None] = lambda event: _process_command(window_console_command_entry, window_console_text)
    window_console_command_entry.bind("<Return>", process_command)
    window_console_command_entry_button: tkinter.Button = tkinter.Button(master=window_console_frame, text="Enter")
    window_console_command_entry_button.bind("<Button-1>", process_command)

    window_console_command_entry_button.grid(row=6, column=5, columnspan=2, sticky="we")

    WINDOW_VIEWER_X: int = WINDOW_CONSOLE_X + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH
    WINDOW_VIEWER_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_VIEWER_HEIGHT) / 2))
    window_viewer: tkinter.Toplevel = tkinter.Toplevel(window_console)
    window_viewer.title(WINDOW_VIEWER_TITLE)
    window_viewer.geometry(f"{WINDOW_VIEWER_WIDTH}x{WINDOW_VIEWER_HEIGHT}+{WINDOW_VIEWER_X}+{WINDOW_VIEWER_Y}")
    # tkinter.PhotoImage

    window_console.focus_force()
    window_root.mainloop() 

def _process_command(command_entry: tkinter.Entry, console_text: tkinter.Text) -> None:
    text: str = command_entry.get()
    command_entry.delete(0, "end")  
    console_text.config(state="normal")
    console_text.insert("end", f"{text}\n")
    console_text.see("end")
    console_text.config(state="disabled")

def run_command(line: str) -> None:



if __name__ == "__main__":
    run()
