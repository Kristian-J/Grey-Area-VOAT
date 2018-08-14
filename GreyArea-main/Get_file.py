
from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter.filedialog import askopenfilename



class SessionFiles:
    def __init__(self, origin):
        self.origin = origin
        self.files_list = self.origin.files
        self.window = origin.root1
            ### asigns the main window identifier to self.window
        self.local_frame = Frame(origin.disp_frame) ### creates a frame hosted the display frame of the main window
        self.local_frame.grid(row = 0, column=0) ### "packs" or "displays" frame

        if self.origin.tf_active:
            return
        elif self.origin.df_active:
            return
        else:
            self.origin.df_active = True
            print('tf set true')
            self.select_files()

        return

    def select_files(self):
        label = Label(self.local_frame, text="please select your file(s)").grid(row=0, column=0, columnspan=3)

        U_input_enter = Button(self.local_frame, text="File")
        U_input_enter.grid(row=1, column=0)
        U_input_enter.bind("<Button-1>", self.get_file_name)
            ### this will bind the button to mouse button 1 (left click) and call the get_file_name

        U_input_exit = Button(self.local_frame, text="Done")
        U_input_exit.grid(row=1,column=1)
        U_input_exit.bind("<Button-1>", self.quit_loop)

    def get_file_name(self, event=NONE):

        if self.origin.ftype == "img":
        # print("function has been called \n")
            name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                   filetypes=(("Jpg files", "*.jpg"), ("PNG files", "*.png"), ("EPS", "*.eps"), ("All Files", "*.*")),
                                   title="Choose a file."
                                   )
        else:
            name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                   filetypes=(("video files", ("*.avi", "*.mp4")), ("All Files", "*.*")),
                                   title="Choose a file."
                                   )

        try: # Using try in case user types in unknown file or closes without choosing a file.
            # with open(name, 'r') as UseFile:
                # print(UseFile.read())
            print("you entered: ", name)
        except:
            print("No file exists")
        if name in self.files_list:
            pass
        elif len(name) <3:
            pass
        else:
            self.files_list.append(name)
        print("files selected are: ", self.files_list)
        return

    def quit_loop(self, event=NONE):
        self.origin.df_active = False
        self.origin.files = self.files_list
        try:
            self.origin.tempframe2.destroy()
        except:
            pass
        self.origin.disp_files()
        self.local_frame.destroy()
        # self.local.quit()
        # self.window.quit()
        # exit()
        return
