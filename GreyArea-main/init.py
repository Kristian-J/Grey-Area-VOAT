# import tkinter as tk
# tk._test()

from tkinter import *
from tkinter import ttk
from Tag_Builder import *
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

        ### variables for storing new ROI information
        self.temp_start_x = None
        self.temp_start_y = None
        self.temp_end_x = None
        self.temp_end_y = None
        self.temp_obj_tags = []
        self.temp_obj = None

        self.vis_objects = []

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

    def disp_tags(self):
        self.tempframe1 = Frame(self.tags_frame)
        self.tempframe1.grid()
        if len(self.tags) > 0:
            for i in self.tags:
                self.tempbutton = Button(self.tempframe1, text=i ,width=15, command = partial(self.disp_obj_tag, i))
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
            pass
        self.local_frame= Frame(self.disp_frame)
        self.local_frame.grid()
        self.image_name = fname

        image = cv2.imread(self.image_name) ### imports the image
        if self.temp_end_x is not None and self.temp_start_x is not None:
            cv2.rectangle(image, (self.temp_start_x, self.temp_start_y), (self.temp_end_x, self.temp_end_y),(0, 0, 255), 4)
        if len(self.vis_objects)>=1:
            # print(self.vis_objects, len(self.vis_objects))
            for i in self.vis_objects:
                print(i)
                coords = i[0]
                print("visobj coords: ", coords)
                cv2.rectangle(image, (coords[0], coords[1]), (coords[2], coords[3]),(200, 0, 0), 4)
                print("visobj coords: ", coords)

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
        print('at bind3',self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y)
        self.disp_img(self.image_name)
        # self.temp_obj[0] = [self.temp_start_x, self.temp_start_y, self.temp_end_x, self.temp_end_y] ### redundant
        # print("tempobj = ",self.temp_obj)

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
            if self.temp_start_x is not None and self.temp_end_x is not None and len(self.temp_obj_tags) >=1 :
                self.temp_obj = [[self.temp_start_x, self.temp_start_y,self.temp_end_x,self.temp_end_y],self.temp_obj_tags]
                self.vis_objects.append(self.temp_obj)
                self.reset_temp_obj()
            # print('temp_obj', self.temp_obj)
            # print("vis_objects", self.vis_objects)
            # if len(self.temp_obj_tags) <= 0:
            #     print("error 3")
            # else:
            #     local = [self.temp_start_x, self.temp_start_y,self.temp_end_x,self.temp_end_y  ]
            #     print(local)
        return

    def disp_obj_tag(self, i):
        counter = 0
        if self.temp_start_x is None:
            return
        elif i is None:
            pass
        elif i not in self.temp_obj_tags:
            self.temp_obj_tags.append(i)
        try:
            self.tempframe3.destroy()
        except:
            print('failed to destroy')
        self.tempframe3 = Frame(self.root1)
        self.tempframe3.grid(row=8, column=1,  columnspan = 9, sticky=NE)
        # print('test deliver tags', self.temp_obj_tags, len(self.temp_obj_tags))
        if len(self.tags) > 0:
            for i in self.temp_obj_tags:
                print(i)
                counter+=1
                self.tempbutton = Button(self.tempframe3, text=i, width=15, command = partial(self.del_obj_tag, i))
                self.tempbutton.grid(row = 0, column = counter, sticky=N)
    def del_obj_tag(self, i):
        # counter = 0
        for item in self.temp_obj_tags:
            if item == i:
                # print(i, item, counter)
                self.temp_obj_tags.remove(item)
                self.disp_obj_tag(None)
                return
            else:
                pass
            # counter += 1

    def reset_temp_obj(self):
        self.temp_start_x = None
        self.temp_start_y = None
        self.temp_end_x = None
        self.temp_end_y = None
        self.temp_obj_tags = []
        self.temp_obj = None
        try:
            self.tempframe3.destroy()
        except:
            pass
        return


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