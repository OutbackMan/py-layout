# import config-variables as ITEST_ConfigVariables

import tkinter

def gui_render() -> None:
  #  ROOT_WINDOW_TITLE: str = f"{ITEST_ConfigVariables.META.name} ({'DEBUG' if __debug__ else 'RELEASE'}) - {ITEST_ConfigVariables.META.version}"
    ROOT_WINDOW_TITLE: str = "TITLE"
    root_window = tkinter.Tk()
    root_window.title(ROOT_WINDOW_TITLE)
    root_window.geometry("400x400")

    text_field = tkinter.Text(root_window, height=10, width=30)
    text_field.grid()

    root_window.mainloop() 

# use grid geometry manager
# sticky indicates what side the element will go to on its container
# NW --> top left

# make (0, 0) expand to containing element (accounts for resize)

# variable class to hold data
    '''
    # left, top, right, bottom
    main_frame = tkinter.Frame(root_window, padding="3 3 12 12")
    main_frame.grid(column=0, row=0)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    '''
'''
feet = tkinter.StringVar()
metres = tkinter.StringVar()

feet_entry = tkinter.ttk.Entry(ui_main_frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky="WE")
tkinter.ttk.Label(ui_main_frame, textvariable=metres).grid(column=2, row=2, stickY="WE")
'''

if __name__ == "__main__":
    gui_render()
