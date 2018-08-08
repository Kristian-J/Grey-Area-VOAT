

from tkinter import *
from tkinter import ttk
from functools import partial


class VisualObject:
    def __init__(self, obj_xy, obj_tags, host_frame):
        self.p1_x = obj_xy[0]
        self.p1_y = obj_xy[1]
        self.p2_x = obj_xy[2]
        self.p2_y = obj_xy[3]
        self.obj_location = obj_xy
        self.obj_tags = obj_tags
        self.host_frame = host_frame
        self.local_frame = None
        self.active = False
        self.file = None

    def add_tag(self, i):
        if i not in self.obj_tags:
            self.obj_tags.append(i)
        self.disp_tags()
    def disp_tags(self):
        try:
            self.local_frame.destroy()
        except:
            print('failed to destroy')

        self.local_frame = Frame(self.host_frame)
        self.local_frame.grid(row=8, column=1,  columnspan = 9, sticky=NE)
        counter = 0
        if len(self.obj_tags) >= 1:
            for i in self.obj_tags:
                print(i)
                counter+=1
                self.tempbutton = Button(self.local_frame, text=i, width=15, command = partial(self.del_obj_tag, i))
                self.tempbutton.grid(row = 0, column = counter, sticky=N)

    def del_obj_tag(self, i):
        # counter = 0
        for item in self.obj_tags:
            if item == i:
                # print(i, item, counter)
                self.obj_tags.remove(item)
                self.disp_tags()
                return
            else:
                pass
            # counter += 1

    def check_inside(self, point):
        pass
        if self.check_between(point[0], self.p1_x, self.p2_x) and self.check_between(point[1], self.p1_y, self.p2_y):
            return True
        else:
            return False
        print("point check error")

    def check_between(self, n, a, b):
        if a > n > b or a < n < b:
            return True
        else:
            return False
