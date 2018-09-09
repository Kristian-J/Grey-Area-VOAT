
import cv2
from tkinter import *
from functools import partial


class Xxxxx:
    def __init__(self, origin):
        self.variable1 = None ### unused variable
        self.U_input = None
            ### variable to hold user input field
            ### created here so it is available to all functions
        self.window = origin.root1
            ### asigns the main window identifier to self.window
            ### this is used to place items in the original window
        self.local_frame = Frame(self.window)
        self.local_frame.grid()

        self.test_function()

        return

    def test_function(self):
        label = Label(self.local_frame, text="this is the local frame").grid(row=0, column=0, columnspan=3)

        self.U_input = Entry(self.local_frame, width=20, )
        self.U_input.grid(row=2, column=1)
            ### example user input field

        U_input_enter = Button(self.local_frame, text="enter")
        U_input_enter.grid(row=2, column=2)
            ### example button
        U_input_enter.bind("<Button-1>", self.some_function)
            ### this will bind the button to mouse button 1 (left click) and call the some_function

    def some_function(self, event=NONE):
        print("function has been called \n")
        user_input = self.U_input.get()
            ### retrieves the contents of the user input field and stores it in the variable
        print("you entered: ", user_input)
        self.local_frame.destroy()
        return