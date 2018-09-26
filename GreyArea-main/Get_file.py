
from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter.filedialog import askopenfilename



class SessionFiles:
    def __init__(self, files, root1, disp_frame, files_frame, ftype, set_active, img_call, disp_vid): # (self, origin)
        # self.origin = origin
        self.files_list = files
        self.window = root1 # = origin.root1
            ### asigns the main window identifier to self.window
        self.disp_frame = disp_frame
        self.files_frame = files_frame
        self.tempframe2= Frame(self.files_frame)
        self.tempframe2.grid()
        self.ftype = ftype
        self.img_call = img_call
        self.disp_vid = disp_vid
        self.set_active = set_active
        # if self.origin.df_active:
        #     return
        # else:
        #     self.origin.df_active = True
        #     print('tf set true')
        self.exist = False ### flag. Used by self.local_file_list function to determin if file item(s) need to be displayed

        self.select_files()

        return

    def select_files(self):
        self.set_active(True)
        self.local_frame = Frame(self.disp_frame) ### creates a frame hosted the display frame of the main window
        self.local_frame.grid(row = 0, column=0) ### "packs" or "displays" frame

        label = ttk.Label(self.local_frame, text="please select your file(s)").grid(row=0, column=0, columnspan=3)

        U_input_enter = ttk.Button(self.local_frame, text="File")
        U_input_enter.grid(row=1, column=0)
        U_input_enter.bind("<Button-1>", self.get_file_name)
            ### this will bind the button to mouse button 1 (left click) and call the get_file_name

        U_input_exit = ttk.Button(self.local_frame, text="Done")
        U_input_exit.grid(row=1,column=1)
        U_input_exit.bind("<Button-1>", self.quit_loop)
        if self.exist:
            self.local_file_list()


    def get_file_name(self, event=NONE):

        if self.ftype == "img":
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
        elif len(name) < 3:
            pass
        else:
            self.files_list.append(name)
        print("files selected are: ", self.files_list)

        self.local_file_list()
        return

    def quit_loop(self, event=NONE):
        self.set_active(False)
        # self.origin.files = self.files_list
        # try:
        #     self.tempframe2.destroy()
        # except:
        #     pass
        self.disp_files()
        self.local_frame.destroy()
        # self.local.quit()
        # self.window.quit()
        # exit()
        return


    def disp_files(self):
        try:
            print("attempting to destroy frame")
            self.tempframe2.destroy()
        except:
            print('failed to destroy frame')
            pass
        print('the files are as such: ', self.files_list)
        self.tempframe2 = Frame(self.files_frame)
        self.tempframe2.grid(sticky=N, padx = 10)
        if len(self.files_list) > 0:
            if self.ftype == 'img':
                for i in self.files_list:
                    self.tempbutton = ttk.Button(self.tempframe2, text=i ,width=20, command = partial(self.img_call, i))
                    self.tempbutton.grid(column=0)
            else:
                for i in self.files_list:
                    self.tempbutton = ttk.Button(self.tempframe2, text=i ,width=20, command = partial(self.disp_vid, i))
                    self.tempbutton.grid(column=0)
        return


    def del_button(self, i):
        # counter = 0
        for item in self.files_list:
            if item == i:
                # print(i, item, counter)
                self.files_list.remove(item)
                self.local_file_list()
                return
            else:
                pass
            # counter += 1


    def local_file_list(self):
        if self.exist:
            self.frame1.destroy()
            print('destroyed')
        self.frame1=Frame(self.local_frame)
        self.frame1.grid(row = 3, column=0, columnspan= 2)
        for i in self.files_list:
            self.tempbutton = ttk.Button(self.frame1, text=i ,width=20, command = partial(self.del_button, i))
            self.tempbutton.grid(column=1)
            # self.tempbutton.bind("<Button-1>")
        self.exist = True
        return
