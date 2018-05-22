
from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter.filedialog import askopenfilename



class SessionFiles:
    def __init__(self, origin):
        self.files = []
        self.U_input = None
            ### variable to hold user input field
            ### created here so it is available to all functions
        self.window = origin.root1
            ### asigns the main window identifier to self.window
            ### this is used to place items in the original window

        self.local_frame = Frame(self.window) ### creates a frame hosted the main window
        self.local_frame.grid() ### "packs" or displays frame

        self.get_files()

        return

    def get_files(self):
        label = Label(self.local_frame, text="this is the local frame").grid(row=0, column=0, columnspan=3)

        U_input_enter = Button(self.local_frame, text="enter")
        U_input_enter.grid(row=2, column=2)
        U_input_enter.bind("<Button-1>", self.some_function)
            ### this will bind the button to mouse button 1 (left click) and call the some_function

        U_input_exit = Button(self.local_frame, text="exit")
        U_input_exit.grid(column=2)
        U_input_exit.bind("<Button-1>", self.quit_loop)

    def some_function(self, event=NONE):
        print("function has been called \n")

        name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                               filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        # print(name)
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            # with open(name, 'r') as UseFile:
                # print(UseFile.read())
            print("you entered: ", name)
        except:
            print("No file exists")
        self.files.append(name)
        print("files selected are: ", self.files)
        return

    def quit_loop(self, event=NONE):
        # self.local.quit()
        self.local_frame.destroy()
        self.window.quit()
        # exit()
        return
