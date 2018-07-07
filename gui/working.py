# can also do: tkinter.mainloop()
import tkinter

console_window: tkinter.Tk = tkinter.Tk()
SCREEN_WIDTH: int = root_window.winfo_screenwidth()
SCREEN_HEIGHT: int = root_window.winfo_screenheight()

CONSOLE_WINDOW_WIDTH: int = 600
CONSOLE_WINDOW_HEIGHT: int = 600
CONSOLE_WINDOW_TITLE: str = "CONSOLE"

VIEWER_WINDOW_WIDTH: int = 600
VIEWER_WINDOW_HEIGHT: int = 600
VIEWER_WINDOW_TITLE: str = "VIEWER"
VIEWER_WINDOW_PAD_X: int = 50

CONSOLE_WINDOW_X = (SCREEN_WIDTH / 2) - ((CONSOLE_WINDOW_WIDTH + VIEWER_WINDOW_WIDTH) / 2)
CONSOLE_WINDOW_Y = (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2)
VIEWER_WINDOW_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 2)
VIEWER_WINDOW_Y = (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2)

root_window.title(ROOT_WINDOW_TITLE)
root_window.geometry(f"{CONSOLE_WINDOW_WIDTH}x{CONSOLE_WINDOW_HEIGHT}+{CONSOLE_WINDOW_X}+{CONSOLE_WINDOW_Y}")

viewer_window = tkinter.Toplevel(console_window)
viewer_window.title("TITLE2")
viewer_window.geometry("400x400")


tkinter.Entry(root_window, width=60).grid(row=0, column=0, columnspan=9, padx=20, pady=20)
tkinter.Button(root_window, text="Enter").grid(row=0, column=10, padx=2, pady=2)
tkinter.Entry(root_window, width=60).grid(row=1, column=0, columnspan=9)
tkinter.Button(root_window, text="Enter2").grid(row=1, column=10, padx=2, pady=2)



'''
main_frame = tkinter.Frame(root_window, padx=12, pady=3)
main_frame.grid(column=0, row=0)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

text = tkinter.text(state="readonly")

text_field = tkinter.Text(root_window, height=10, width=30)
text_field.grid()
'''

root_window.mainloop() 
