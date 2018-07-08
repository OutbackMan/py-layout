# can also do: tkinter.mainloop()
import tkinter
import typing

def gui_run() -> None:
    WINDOW_CONSOLE_WIDTH: int = 600
    WINDOW_CONSOLE_HEIGHT: int = 600
    WINDOW_CONSOLE_TITLE: str = "CONSOLE"

    WINDOW_VIEWER_WIDTH: int = 600
    WINDOW_VIEWER_HEIGHT: int = 600
    WINDOW_VIEWER_TITLE: str = "VIEWER"

    WINDOW_MARGIN_WIDTH: int = 50

    window_root: tkinter.Tk = tkinter.Tk()
    window_root.grid_rowconfigure(0, weight=1)
    window_root.grid_columnconfigure(0, weight=1)
    SCREEN_WIDTH: int = window_root.winfo_screenwidth()
    SCREEN_HEIGHT: int = window_root.winfo_screenheight()

    WINDOW_TOTAL_WIDTH: int = WINDOW_CONSOLE_WIDTH + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH

    WINDOW_CONSOLE_X: int = int((SCREEN_WIDTH / 2) - ((WINDOW_TOTAL_WIDTH) / 2))
    WINDOW_CONSOLE_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_CONSOLE_HEIGHT) / 2))
    window_console: tkinter.Tk = window_root
    window_console.title(WINDOW_CONSOLE_TITLE)
    window_console.geometry(f"{WINDOW_CONSOLE_WIDTH}x{WINDOW_CONSOLE_HEIGHT}+{WINDOW_CONSOLE_X}+{WINDOW_CONSOLE_Y}")
    window_console_frame: tkinter.Frame = tkinter.Frame(master=window_console, padx=12, pady=12)
    window_console_frame.grid(column=0, row=0, sticky="nsew")

    window_console_frame.grid_columnconfigure(0, weight=10)
    window_console_frame.grid_columnconfigure(1, weight=10)
    window_console_frame.grid_columnconfigure(2, weight=10)
    window_console_frame.grid_columnconfigure(3, weight=10)
    window_console_frame.grid_columnconfigure(4, weight=10)
    window_console_frame.grid_columnconfigure(5, weight=10)
    window_console_frame.grid_columnconfigure(6, weight=1)
    window_console_frame.grid_rowconfigure(0, weight=10)
    window_console_frame.grid_rowconfigure(1, weight=10)
    window_console_frame.grid_rowconfigure(2, weight=10)
    window_console_frame.grid_rowconfigure(3, weight=10)
    window_console_frame.grid_rowconfigure(4, weight=10)
    window_console_frame.grid_rowconfigure(5, weight=1)
    window_console_frame.grid_rowconfigure(6, weight=10)

    window_console_text: tkinter.Text = tkinter.Text(master=window_console_frame, wrap="word")
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

    window_console.focus_force()
    window_root.mainloop() 

def _process_command(command_entry: tkinter.Entry, console_text: tkinter.Text) -> None:
    text: str = command_entry.get()
    command_entry.delete(0, "end")  
    console_text.config(state="normal")
    console_text.insert("end", f"{text}\n")
    console_text.see("end")
    console_text.config(state="disabled")


if __name__ == "__main__":
    gui_run()
