import tkinter
# tkinter.ttk --> themed widgets

ui_root_window = tkinter.Tk()
ui_root_window.title("UI")

# left, top, right, bottom
ui_main_frame = tkinter.ttk.Frame(ui_root_window, padding="3 3 12 12")

# use grid geometry manager
# sticky indicates what side the element will go to on its container
# NW --> top left
ui_main_frame.grid(column=0, row=0, sticky="NW")

# make (0, 0) expand to containing element (accounts for resize)
ui_main_frame.columnconfigure(0, weight=1)
ui_main_frame.rowconfigure(0, weight=1)

# variable class to hold data
feet = tkinter.StringVar()
metres = tkinter.StringVar()

feet_entry = tkinter.ttk.Entry(ui_main_frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky="WE")
tkinter.ttk.Label(ui_main_frame, textvariable=metres).grid(column=2, row=2, stickY="WE")
