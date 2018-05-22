
from Get_file import *
from tkinter import *
from functools import partial

class SessionTags:
    def __init__(self, origin):
        # print(origin, origin.response, type(origin.root1))
        self.window = origin.root1
        self.origin = origin
        self.response = None
        self.tag_list = []
        self.exist = False
        self.tempbutton = None
        self.local_frame = None

        self.get_tags()

        return

    def get_tags(self):
        self.local_frame= Frame(self.window )
        self.local_frame.grid()
        Label(self.local_frame, text="Please specify you're object tags").grid(row=0, column=0, columnspan=2)

        U_input_label = Label(self.local_frame, text="Enter tag")
        U_input_label.grid(row=2, column=0,)

        global U_input
        U_input = Entry(self.local_frame, width=20, )
        U_input.grid(row=2, column=1)

        U_input_enter = Button(self.local_frame, text="Enter")
        U_input_enter.grid(row=2, column=2)
        U_input_enter.bind("<Button-1>", self.add_tag)

        U_input_exit = Button(self.local_frame, text="exit")
        U_input_exit.grid(column=2)
        U_input_exit.bind("<Button-1>", self.quit_loop)

    def add_tag(self, event=NONE):
        global U_input
        tag = U_input.get()
        print(tag)
        if len(tag) == 0:
            return
        self.tag_list.append(tag)
        print(self.tag_list)
        U_input.delete(0, "end")
        self.dis_tags()
        return

    def quit_loop(self, event=NONE):
        # self.local.quit()
        self.local_frame.destroy()
        self.origin.session_files = SessionFiles(self.origin)
        # self.window.quit()
        # exit()
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
        self.frame1.grid(column=1)
        for i in self.tag_list:
            self.tempbutton = Button(self.frame1, text=i ,width=20, command = partial(self.del_button, i))
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