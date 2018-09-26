import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from SaveData import *
from functools import partial
from Freature_handler import *


class VidHandler():
    def __init__(self, origin):
        self.origin = origin
        self.file = origin.cnt_vid
        self.vis_objects = self.origin.vis_objects
        self.selected_tracker = self.origin.t_type
        self.obj_tags_frame = self.origin.obj_tags_frame
        self.reset_temp_obj = self.origin.reset_temp_obj
        self.reset_new_obj = self.origin.reset_new_obj
        self.disp_img = self.origin.disp_img
        self.cap = cv2.VideoCapture(self.file)

        self.total_frames = self.cap.get(7)
        print('the numer of frames are: ', self.total_frames)
        self.frame_num = 0
        self.labelmessage = "The current frame is #" + str(self.frame_num)

        self.extract_frame(self.frame_num)
        self.local_frame = Frame(self.origin.controls_frame) # (self.origin.controls_frame)
        self.local_frame.grid(sticky = N)

        # global f_input
        self.labelmsg = "Max frame #:  " + str(self.total_frames - 1)
        # print(labelmsg)

        self.fnum_label = ttk.Label(self.local_frame, text=self.labelmessage)
        self.fnum_label.grid(row=0, column=0, padx = 5)
        style = ttk.Style()
        style.configure("TButton", forground="blue", background="cyan")

        back_jump = ttk.Button(self.local_frame, text = " <<-- ", command = partial(self.go_to_frame, -5) )
        back_jump.grid(row=0, column=1, padx = 5)
        back_step = ttk.Button(self.local_frame, text = " <- ", command = partial(self.go_to_frame, -1))
        back_step.grid(row=0, column=2, padx = 5)
        step = ttk.Button(self.local_frame, text = " -> ", command = partial(self.go_to_frame, 1))
        step.grid(row=0, column=3, padx = 5)
        jump = ttk.Button(self.local_frame, text = " -->> ", command = partial(self.go_to_frame, 5))
        jump.grid(row=0, column=4, padx = 5)

        label = ttk.Label(self.local_frame, text=self.labelmsg)
        label.grid(row=0, column=5)

        frame_sel = ttk.Button(self.local_frame, text="Go to Frame", command=self.get_f_num)
        frame_sel.grid(row=0, column=6)

    def get_f_num(self, event=NONE):
        print("get frame number. here")
        self.temp_frame = Frame(self.local_frame)
        self.temp_frame.grid(row=0, column=7)
        temp_label = ttk.Label(self.temp_frame).grid(row=0, column=0)
        self.f_input = ttk.Entry(self.temp_frame, width=20)
        self.f_input.grid(row=1, column=0)
        self.f_input.bind("<Return>", self.set_f_num)

        f_input_enter = ttk.Button(self.temp_frame, text="Enter")
        f_input_enter.grid(row=1, column=1)
        f_input_enter.bind("<Button-1>", self.set_f_num)

        f_input_back = ttk.Button(self.temp_frame, text="cancel", command=self.back)
        f_input_back.grid(row=0, column=1)

        # global f_input

    def set_f_num(self, event):
        frame_num = self.f_input.get()
        print('the frame number is: ', frame_num, type(frame_num))
        try:
            frame_num = int(frame_num)
        except:
            print('Imput was not a number')
            pass
        if type(frame_num) == int:
            if 0 <= frame_num < self.total_frames:
                if len(self.vis_objects) >= 1:
                    SaveToFile(self.vis_objects, self.file, self.frame_num)
                    # obj_check = FeatureTrack("temp.jpg",self.file, frame_num, self.origin.vis_objects,self.origin.selected_tracker.get(), )
                self.frame_num = frame_num
                self.vis_objects = []
                self.extract_frame(frame_num)
                self.back()
            else:
                print("number out of range")

    def back(self):
        try:
            self.temp_frame.destroy()
        except:
            pass
        return

    def go_to_frame(self, n):
        # print('incoming value = ', self.frame_num)
        frame_num = self.frame_num + n
        # print("self.frame_num = ", self.frame_num)
        if 0 <= frame_num < self.total_frames:
            print('check one')
            if len(self.origin.vis_objects) >= 1:
                print('check two')
                SaveToFile(self.origin.vis_objects, self.origin.cnt_vid, self.frame_num)
                obj_check = FeatureTrack("temp.jpg", self.file, frame_num, self.origin.vis_objects,self.origin.t_type)
            self.frame_num = frame_num
            self.extract_frame(self.frame_num)
        else:
            print("number out of range")
            return

    def extract_frame(self, num):
            for i in self.vis_objects:
                if i.active:
                    i.local_frame.destroy()
            try:
                temptext = str("The current frame is #" + str(self.frame_num))
                self.fnum_label.config(text=temptext)
            except:
                pass
            self.reset_temp_obj()
            self.reset_new_obj()
            self.vis_objects = []

            ### Import existing data if associated data file exists.
            tryload = LoadData(self.file, self.frame_num, self.obj_tags_frame)
            if tryload.load:
                self.vis_objects = tryload.image_objects
                print("the objects are: ", self.vis_objects)
            self.cap.set(1, num)
            print(">>>>>> ", num, "<<<<<<")
            ret, frame = self.cap.read()
            cv2.imwrite('temp.jpg', frame)
            self.disp_img('temp.jpg', self.vis_objects)



# self.reset_temp_obj()
# self.reset_new_obj()
# self.vis_objects = []