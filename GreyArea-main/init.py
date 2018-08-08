# import tkinter as tk
# tk._test()

from tkinter import *
from tkinter import ttk
from Tag_Builder import *
from Visual_object import *
from module_template import *
from Vid_Handle import *
from Img_handle import *
from functools import partial

class Controller:
    def __init__(self, ftype):
        self.ftype = ftype
        self.cnt_vid = None

        self.files =[]  ### list of current filenames
        self.session_tags = None ### for storing the instance of SessionTags
        self.tags =[]  ### list of current tags
        self.session_files = None ### for storing the instance of SessionFiles
        self.image_name = None
        ### creating the main window ###
        self.root1 = Tk() ### creating main window
        self.root1.title("Welcome")
        self.root1.geometry("1400x900")

        ### variables for handling ROI information
        self.temp_start_x = None
        self.temp_start_y = None
        self.temp_end_x = None
        self.temp_end_y = None
        self.temp_tags = []
        self.temp_obj = None

        self.new_start_x = None
        self.new_start_y = None
        self.new_end_x = None
        self.new_end_y = None
        # self.new_obj_tags = []
        self.new_obj = None

        # self.active_start_x = None
        # self.active_start_y = None
        # self.active_end_x = None
        # self.active_end_y = None
        # self.active_obj_tags = []
        self.active_obj = None
        self.active_flag = False

        self.vis_objects = []

        self.point_x = None
        self.point_y = None

        ### variable for holding image scale ratio for ROI scaling.
        self.scale_ratio = 1

        # print(self.root1.winfo_pointerxy())
        ### setting the structure for the window and component elements ###
        self.tags_frame = Frame(self.root1)
        self.tags_frame.grid(row=2, column=0, rowspan= 4, columnspan = 1, sticky=N)
        self.tf_active = False

        ### frame for displaying file name buttons
        self.files_frame = Frame(self.root1)
        self.files_frame.grid(row=0, column=11, rowspan= 10, columnspan = 1, sticky=N)
        self.ff_active = False

        ### frame for main display
        self.disp_frame = Frame(self.root1)
        self.disp_frame.grid(row=0, column=1, rowspan= 7, columnspan = 9,sticky=NE)
        self.df_active = False

        ### frame for positioning the video controls
        self.controls_frame = Frame(self.root1)
        self.controls_frame.grid(row=7, column=1,  columnspan = 9, sticky=NE)
        self.cf_active = False

        ### frame for displaying object tags
        self.obj_tags_frame = Frame(self.root1)
        self.obj_tags_frame.grid(row=8, column=1,  columnspan = 9, sticky=NE)

        # Menu Bar
        self.menu_frame = Frame(self.root1)
        self.menu_frame.grid(row=0, column=0, rowspan= 2,sticky=N)

        menu = Menu(self.root1)
        self.root1.config(menu=menu)

        file = Menu(menu)
        # file.add_command(label='Open', command=OpenFile)
        # file.add_command(label='Exit', command=lambda: exit())
        file.add_command(label='Exit', command=lambda: self.root1.quit())
        menu.add_cascade(label='File', menu=file)

        button3 = Button(self.menu_frame, width=15, text="Add Tags")
        button3.grid(row=1, column=1, sticky=N)
        button3.bind("<Button-1>", self.get_tags)
        button4 = Button(self.menu_frame, width=15, text="Select File")
        button4.grid(row=2, column=1, sticky=N)
        button4.bind("<Button-1>", self.get_files)
        return

    def get_tags(self, event=NONE):
        self.session_tags = SessionTags(self)
        print('these are the current tags', self.tags)
        return
    def get_files(self, event=NONE):
        self.session_files = SessionFiles(self)
        print('these are the current files', self.files)
        return

    def disp_tags(self): ### displays general tag list as buttons
        self.tempframe1 = Frame(self.tags_frame)
        self.tempframe1.grid()
        if len(self.tags) > 0:
            for i in self.tags:
                self.tempbutton = Button(self.tempframe1, text=i ,width=15, command = partial(self.add_temp_tag, i))
                self.tempbutton.grid(sticky=N)

    def disp_files(self):
        self.tempframe2 = Frame(self.files_frame)
        self.tempframe2.grid(sticky=N)
        if len(self.files) > 0:
            if self.ftype == 'img':
                for i in self.files:
                    self.tempbutton = Button(self.tempframe2, text=i ,width=20, command = partial(self.img_call, i))
                    self.tempbutton.grid(column=0)
            else:
                for i in self.files:
                    self.tempbutton = Button(self.tempframe2, text=i ,width=20, command = partial(self.disp_vid, i))
                    self.tempbutton.grid(column=0)

    def img_call(self, fname):
        self.reset_temp_obj()
        self.vis_objects = []
        self.disp_img(fname)

    def disp_vid(self, fname):
        try:
            self.video_disp.local_frame.destroy()
        except:
            pass
        self.cnt_vid = fname
        self.video_disp = VidHandler(self)
        return
    def disp_img(self, fname):
        try:
            self.local_frame.destroy()
        except:
            print("could not destroy local_frame")
            pass
        self.local_frame = Frame(self.disp_frame)
        self.local_frame.grid()
        self.image_name = fname

        image = cv2.imread(self.image_name) ### imports the image
        if self.new_start_x is not None and self.new_end_x is not None:
            cv2.rectangle(image, (self.new_start_x, self.new_start_y), (self.new_end_x, self.new_end_y),(0, 0, 255), 4)
        if len(self.vis_objects)>=1:
            # print(self.vis_objects, len(self.vis_objects))
            for i in self.vis_objects:
                coords = i.obj_location
                print(i, i.active, i.obj_location, i.obj_tags)
                try:
                    i.local_frame.destroy()
                    self.tempframe3.destroy()
                except:
                    pass
                if i.active == True:
                    cv2.rectangle(image, (coords[0], coords[1]), (coords[2], coords[3]),(0, 200, 0), 4)
                    i.disp_tags()
                else:
                    cv2.rectangle(image, (coords[0], coords[1]), (coords[2], coords[3]),(200, 0, 0), 4)
            print(self.vis_objects)
            # print("visobj coords: ", coords)

        # Rearrange the color channel
        b, g, r = cv2.split(image)
        img = cv2.merge((r, g, b))
        # Convert the Image object into a TkPhoto object
        img = Image.fromarray(img)

        basewidth = 1100  ### sets control on image size, with aspect ratio intact
        wpercent = (basewidth / float(img.size[0])) ### image scale ratio
        self.scale_ratio = wpercent
        hsize = int((float(img.size[1]) * float(wpercent)))
        im = img.resize((basewidth, hsize), Image.ANTIALIAS)
        print("image size debug", 'hight is- ', hsize, 'percent is- ', wpercent)
        imgtk = ImageTk.PhotoImage(master = self.local_frame, image=im)

        # Put it in the display window
        label = Label(self.local_frame, image=imgtk)
        label.image = imgtk
        label.grid()

        ### image event handling
        label.bind("<Button-1>", self.bind_click )
        # label.bind("<B1-Motion>", self.bind2 )
        label.bind("<ButtonRelease-1>", self.bind_release )
        # label.bind("<Return>")
        # label.bind("<Leave>")
        self.root1.bind("<KeyPress>",self.keybind)
        self.root1.bind("<BackSpace>", self.bind_backSpace)

        return
    ### image event handling functions
    def bind_click(self, event): ### ROI mouse click event manager
        print('at bind1', event.x, event.y)
        self.temp_start_x = int(event.x//self.scale_ratio)
        self.temp_start_y = int(event.y//self.scale_ratio)
        print('at bind1', self.temp_start_x, self.temp_start_y)
        return
    def bind2(self, event):
        self.temp_end_x = int(event.x//self.scale_ratio)
        self.temp_end_y = int(event.y//self.scale_ratio)
        # print('at bind2',self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y)
        return
    def bind_release(self, event): ### ROI mouse release event manager
        self.temp_end_x = int(event.x//self.scale_ratio)
        self.temp_end_y = int(event.y//self.scale_ratio)
        print('at bind3',self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y, self.image_name)
        # self.disp_img(self.image_name)
        self.coord_validate(self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y)

        # self.temp_obj[0] = [self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y] ### redundant
        # print("tempobj = ",self.temp_obj)
    def bind_backSpace(self,event):
        print('backspace was pressed')
        for i in self.vis_objects:
            if i.active:
                confirm = user_confirm("do you want to remove this object?").response
                if confirm:
                    self.vis_objects.remove(i)
                    try:
                        i.local_frame.destroy()
                    except:
                        pass
                    self.disp_img(self.image_name)
                    self.active_flag = False
                    print("object should have been removed")
                    return
                else:
                    return

    def keybind(self, event): ### image interaction Hotkey handler
        item = event.char
        if item.isalpha():
            pass
        else:
            return
        print(item.isalpha())
        print(">",item,"<")
        if item in ("s","S"):
            print('key is s')
            if self.temp_start_x is not None and self.temp_end_x is not None and len(self.temp_tags) >=1 :

                self.temp_obj = [self.temp_start_x, self.temp_start_y,self.temp_end_x,self.temp_end_y]
                self.new_obj = VisualObject(self.temp_obj, self.temp_tags, self.obj_tags_frame)
                # print("this is the oject: ", self.new_obj)
                if len(self.vis_objects) >= 1:
                    for i in self.vis_objects:
                        i.active = False
                self.new_obj.active = True
                self.active_flag = True
                self.vis_objects.append(self.new_obj)
                self.reset_temp_obj()
                self.disp_img(self.image_name)

            # print('temp_obj', self.temp_obj)
            # print("vis_objects", self.vis_objects)
            # if len(self.temp_tags) <= 0:
            #     print("error 3")
            # else:
            #     local = [self.temp_start_x, self.temp_start_y,self.temp_end_x,self.temp_end_y  ]
            #     print(local)
        return

    def add_temp_tag(self, i):
        if self.active_flag:
            print("flag is active")
            for obj in self.vis_objects:
                if obj.active:
                    obj.add_tag(i)
        else:
            if self.temp_start_x is None or self.temp_end_x is None:
                return
            elif i is None:
                pass
            elif i not in self.temp_tags:
                self.temp_tags.append(i)
            self.disp_temp_tags()

    def disp_temp_tags(self):
        try:
            self.tempframe3.destroy()
        except:
            print('failed to destroy')
        self.tempframe3 = Frame(self.obj_tags_frame)
        self.tempframe3.grid()

        counter = 0
        if len(self.tags) >= 1:
            for i in self.temp_tags:
                print(i)
                counter+=1
                self.tempbutton = Button(self.tempframe3, text=i, width=15, command = partial(self.del_obj_tag, i))
                self.tempbutton.grid(row = 0, column = counter, sticky=N)

    def del_obj_tag(self, i):
        # counter = 0
        for item in self.temp_tags:
            if item == i:
                # print(i, item, counter)
                self.temp_tags.remove(item)
                self.disp_temp_tags()
                return
            else:
                pass
            # counter += 1

    def coord_validate(self, p1x, p1y, p2x, p2y):
        if abs(p1x - p2x)< 10 and abs(p1y - p2y)< 10:
            print(abs(p1x - p2x))
            self.point_x = p1x
            self.point_y = p1y
            """need to add conditional check. if temp_tags is not empty, and a new (unsaved) ROI exists or active object has been modified, check if user wants to save the object """
            self.reset_temp_obj()
            self.reset_new_obj()
            point = [self.point_x, self.point_y]
            print("coord val debug - vis-objs: ", self.vis_objects)
            if len(self.vis_objects) >=1:
                flag = False
                for o in self.vis_objects:
                    # print('object: ', i)
                    if o.check_inside([self.point_x, self.point_y]):
                        if o.active:
                            o.active = False
                        else:
                            if not flag:
                                o.active = True
                                flag = True
                    else:
                        o.active = False
                if flag:
                    self.active_flag = True
                else:
                    self.active_flag = False

            self.disp_img(self.image_name)


        elif abs(p1x - p2x)< 10 and abs(p1y - p2y)> 10 or abs(p1x - p2x)> 10 and abs(p1y - p2y)< 10 :
            print("invalid ROI")
            self.reset_temp_obj()
            self.reset_new_obj()
            self.active_flag = False
            ### invalid ROI
            return
        else:
            self.new_start_x = p1x
            self.new_start_y = p1y
            self.new_end_x = p2x
            self.new_end_y = p2y
            for i in self.vis_objects:
                i.active = False
            self.active_flag = False
            self.disp_img(self.image_name)
            print("new coordinates are", self.new_start_x, self.new_start_y, self.new_end_x, self.new_end_y)


    def reset_temp_obj(self):
        self.temp_start_x = None
        self.temp_start_y = None
        self.temp_end_x = None
        self.temp_end_y = None
        self.temp_tags = []
        self.temp_obj = None
        try:
            self.tempframe3.destroy()
        except:
            pass
        return

    def reset_new_obj(self):
        self.new_start_x = None
        self.new_start_y = None
        self.new_end_x = None
        self.new_end_y = None


class GetType():
    def __init__(self):
        print("this it the type control")
        self.response = None

        self.root0 = Tk()
        self.frame = Frame(self.root0)
        self.frame.grid(row = 0, column = 0)
        Label(self.frame, text="Are you working with image or video files today?").grid(row=0, column=0, columnspan=2)

        button1 = Button(self.frame, width=20, height=5, text="Image")
        button1.grid(row=1, column=0, sticky=N)
        button1.bind("<Button-1>", self.ftypeim)

        button2 = Button(self.frame, width=20, height=5, text="Video")
        button2.grid(row=1, column=1, sticky=N)
        button2.bind("<Button-1>", self.ftypevid)

        self.root0.mainloop()
    def ftypeim(self, event=NONE):
        self.response = "img"
        # print("img?")
        self.quit_loop()
    def ftypevid(self, event=NONE):
        self.response = "vid"
        # print("vid?")
        self.quit_loop()

    def quit_loop(self, event=NONE):
        self.root0.withdraw()
        self.frame.destroy()
        self.root0.quit()
        return

class user_confirm():
    def __init__(self, string):
        self.question = string
        self.response = None
        self.local_root1 = Tk()
        self.local_root1.title("Welcome")
        self.local_root1.geometry("300x300")
        label = Label(self.local_root1, text=self.question).grid(row=0, column=0, columnspan=2)
        self.positive = Button(self.local_root1, width=20, height=5, text="Continue", command = partial(self.assign_response, True))
        self.positive.grid(row=1, column=0, sticky=N)

        self.negative = Button(self.local_root1, width=20, height=5, text="Cancel", command = partial(self.assign_response, False))
        self.negative.grid(row=1, column=1, sticky=N)
        self.local_root1.mainloop()
    def assign_response(self, response, event=NONE):
        self.response = response
        print("the user response is: ", self.response)
        self.quit_loop()
    def quit_loop(self, event=NONE):
        self.local_root1.withdraw()
        self.local_root1.quit()

f_type = GetType()
while f_type.response == None:
    f_type = GetType()
control_type = f_type.response
print(control_type)
primary = Controller(control_type)
# session_tags = primary.session_tags
# session_tags = SessionTags(primary)

primary.root1.mainloop()

print (f_type.response, 'session tags: ', primary.session_tags.tag_list, primary.session_tags.response, primary.session_tags.exist, "The End")
try:
    print("selected files are: ", primary.files)
    print("selected tags are: ", primary.tags)
except:
    print("error: data not stored in variable.")





### example code section for file import handling
### https://gist.github.com/Yagisanatode/0d1baad4e3a871587ab1