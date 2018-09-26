
from Get_file import *
from tkinter import *
from functools import partial

class SessionTags:
    # def __init__(self, origin):
    def __init__ (self, tag_list, host_frame, set_active, disp_tags):
        # print(origin, origin.response, type(origin.root1))
        self.set_active = set_active
        self.disp_tags = disp_tags
        # self.origin = origin
        self.response = None
        self.tag_list = tag_list #self.origin.tags
        self.exist = False
        self.tempbutton = None
        self.local_frame = Frame(host_frame) # Frame(self.origin.disp_frame)

        self.style = ttk.Style()
        self.style.configure("TButton", forground="blue", background="cyan")


        self.set_active(True)
        if len(self.tag_list) >= 1: # len(self.origin.tags) >=1:
            self.dis_tags()
        # if self.origin.df_active:
        #     return
        # else:
        #     self.origin.df_active = True
        #     print('tf set true')
        self.select_tags()
        return

    def select_tags(self):
        self.local_frame.grid(row=0, column=0)
        ttk.Label(self.local_frame, text="Please specify you're object tags").grid(row=0, column=0, columnspan=2)

        U_input_label = ttk.Label(self.local_frame, text="Enter tag")
        U_input_label.grid(row=2, column=0,)

        global U_input
        U_input = ttk.Entry(self.local_frame, width=20 )
        U_input.grid(row=2, column=1)
        U_input.bind("<Return>", self.add_tag)

        U_input_enter = ttk.Button(self.local_frame, text="Enter")
        U_input_enter.grid(row=2, column=2)
        U_input_enter.bind("<Button-1>", self.add_tag)

        U_input_exit = ttk.Button(self.local_frame, text="Done")
        U_input_exit.grid(row= 3,column=2, sticky = N)
        U_input_exit.bind("<Button-1>", self.quit_loop)

    def add_tag(self, event=NONE):
        global U_input
        tag = U_input.get()
        print(tag)
        if len(tag) == 0:
            return
        if tag in self.tag_list:
            pass
        else:
            self.tag_list.append(tag)
        print(self.tag_list)
        U_input.delete(0, "end")
        self.dis_tags()
        return

    def quit_loop(self, event=NONE):
        self.set_active(False) # self.origin.df_active = False
        print('tf set false')
        # self.origin.tags = self.tag_list
        self.disp_tags() # self.origin.disp_tags()
        self.local_frame.destroy()
        return

    def del_button(self, i):
        # counter = 0
        for item in self.tag_list:
            if item == i:
                # print(i, item, counter)
                self.tag_list.remove(item)
                self.dis_tags()
                return
            else:
                pass
            # counter += 1


    def dis_tags(self):
        if self.exist:
            self.frame1.destroy()
            print('destroyed')
        self.frame1=Frame(self.local_frame)
        self.frame1.grid(row = 3, column=1)
        for i in self.tag_list:
            self.tempbutton = ttk.Button(self.frame1, text=i ,width=20, command = partial(self.del_button, i))
            self.tempbutton.grid(column=1)
            # self.tempbutton.bind("<Button-1>")
        self.exist = True
        return





# tag_list = ["jack","flash"]
# root = Tk()
# session = File_Type()
#
# root.mainloop()
#
# print('end', session.tag_list)