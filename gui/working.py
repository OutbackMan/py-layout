# can also do: tkinter.mainloop()
import tkinter

def gui_run() -> None:
    WINDOW_CONSOLE_WIDTH: int = 600
    WINDOW_CONSOLE_HEIGHT: int = 600
    WINDOW_CONSOLE_TITLE: str = "CONSOLE"

    WINDOW_VIEWER_WIDTH: int = 600
    WINDOW_VIEWER_HEIGHT: int = 600
    WINDOW_VIEWER_TITLE: str = "VIEWER"

    WINDOW_MARGIN_WIDTH: int = 50

    window_root: tkinter.Tk = tkinter.Tk()
    SCREEN_WIDTH: int = window_root.winfo_screenwidth()
    SCREEN_HEIGHT: int = window_root.winfo_screenheight()

    WINDOW_TOTAL_WIDTH: int = WINDOW_CONSOLE_WIDTH + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH

    WINDOW_CONSOLE_X: int = int((SCREEN_WIDTH / 2) - ((WINDOW_TOTAL_WIDTH) / 2))
    WINDOW_CONSOLE_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_CONSOLE_HEIGHT) / 2))
    window_console: tkinter.Tk = window_root
    window_console.title(WINDOW_CONSOLE_TITLE)
    window_console.geometry(f"{WINDOW_CONSOLE_WIDTH}x{WINDOW_CONSOLE_HEIGHT}+{WINDOW_CONSOLE_X}+{WINDOW_CONSOLE_Y}")

    window_console_menu: tkinter.Menu = tkinter.Menu(window_console)
    window_console_menu_file: tkinter.Menu = tkinter.Menu(window_console_menu, tearoff=0)
    window_console_menu.add_cascade(label="File", menu=window_console_menu_file)
    window_console.config(menu=window_console_menu)

    WINDOW_VIEWER_X: int = WINDOW_CONSOLE_X + WINDOW_MARGIN_WIDTH + WINDOW_VIEWER_WIDTH
    WINDOW_VIEWER_Y: int = int((SCREEN_HEIGHT / 2) - ((WINDOW_VIEWER_HEIGHT) / 2))
    window_viewer: tkinter.Toplevel = tkinter.Toplevel(window_console)
    window_viewer.title(WINDOW_VIEWER_TITLE)
    window_viewer.geometry(f"{WINDOW_VIEWER_WIDTH}x{WINDOW_VIEWER_HEIGHT}+{WINDOW_VIEWER_X}+{WINDOW_VIEWER_Y}")

    window_root.mainloop() 
'''
tkinter.Entry(root_window, width=60).grid(row=0, column=0, columnspan=9, padx=20, pady=20)
tkinter.Button(root_window, text="Enter").grid(row=0, column=10, padx=2, pady=2)
tkinter.Entry(root_window, width=60).grid(row=1, column=0, columnspan=9)
tkinter.Button(root_window, text="Enter2").grid(row=1, column=10, padx=2, pady=2)
'''



'''
main_frame = tkinter.Frame(root_window, padx=12, pady=3)
main_frame.grid(column=0, row=0)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

text = tkinter.text(state="readonly")

text_field = tkinter.Text(root_window, height=10, width=30)
text_field.grid()
'''

if __name__ == "__main__":
    gui_run()
