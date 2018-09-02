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
        self.cap = cv2.VideoCapture(self.file)
        self.total_frames = self.cap.get(7)
        print('the numer of frames are: ', self.total_frames)
        self.frame_num = 0
        self.labelmessage = "The current frame is #" + str(self.frame_num)
        self.extract_frame(self.frame_num)
        self.local_frame = Frame(self.origin.controls_frame)
        self.local_frame.grid(sticky = N)

        global f_input
        labelmsg = "Max frame #:  " + str(self.total_frames - 1)
        # print(labelmsg)

        self.fnum_label = ttk.Label(self.local_frame, text=self.labelmessage)
        self.fnum_label.grid(row=0, column=0, padx = 5)

        back_jump = ttk.Button(self.local_frame, text = " <<-- ", command = partial(self.go_to_frame, -5) )
        back_jump.grid(row=0, column=1, padx = 5)
        back_step = ttk.Button(self.local_frame, text = " <- ", command = partial(self.go_to_frame, -1))
        back_step.grid(row=0, column=2, padx = 5)
        step = ttk.Button(self.local_frame, text = " -> ", command = partial(self.go_to_frame, 1))
        step.grid(row=0, column=3, padx = 5)
        jump = ttk.Button(self.local_frame, text = " -->> ", command = partial(self.go_to_frame, 5))
        jump.grid(row=0, column=4, padx = 5)

        label = ttk.Label(self.local_frame, text=labelmsg)
        label.grid(row=0, column=5)
        f_input = ttk.Entry(self.local_frame, width=20 )
        f_input.grid(row=0, column=6)
        f_input.bind("<Return>", self.set_f_num)

        f_input_enter = ttk.Button(self.local_frame, text="Enter")
        f_input_enter.grid(row=0, column=7)
        f_input_enter.bind("<Button-1>", self.set_f_num)

    def set_f_num(self, event=NONE):
        global f_input
        frame_num = f_input.get()
        # print('the frame number is: ', frame_num, type(frame_num))
        try:
            frame_num = int(frame_num)
        except:
            print('Imput was not a number')
            pass
        if type(frame_num) == int:
            if 0 <= frame_num < self.total_frames:
                if len(self.origin.vis_objects) >= 1:
                    SaveToFile(self.origin.vis_objects, self.origin.cnt_vid, self.frame_num)
                    obj_check = FeatureTrack("temp.jpg",self.file, frame_num, self.origin.vis_objects,self.origin.selected_tracker.get(), )
                self.frame_num = frame_num
                self.extract_frame(frame_num)
            else: print("number out of range")

    def go_to_frame(self, n):
        # print('incoming value = ', self.frame_num)
        frame_num = self.frame_num + n
        # print("self.frame_num = ", self.frame_num)
        if 0 <= frame_num < self.total_frames:
            if len(self.origin.vis_objects) >= 1:
                SaveToFile(self.origin.vis_objects, self.origin.cnt_vid, self.frame_num)
                obj_check = FeatureTrack("temp.jpg", self.file, frame_num, self.origin.vis_objects,self.origin.selected_tracker.get())
            self.frame_num = frame_num
            self.extract_frame(self.frame_num)
        else:
            print("number out of range")
            return

    def extract_frame(self, num):
            for i in self.origin.vis_objects:
                if i.active:
                    i.local_frame.destroy()
            try:
                temptext = str("The current frame is #" + str(self.frame_num))
                self.fnum_label.config(text=temptext)
            except:
                pass
            self.origin.reset_temp_obj()
            self.origin.reset_new_obj()
            self.origin.vis_objects = []

            ### Import existing data if associated data file exists.
            tryload = LoadData(self.origin.cnt_vid, self.frame_num, self.origin.obj_tags_frame)
            if tryload.load:
                self.origin.vis_objects = tryload.image_objects
            self.cap.set(1, num)
            print(">>>>>> ", num, "<<<<<<")
            ret, frame = self.cap.read()
            cv2.imwrite('temp.jpg', frame)
            self.origin.disp_img('temp.jpg')



# self.reset_temp_obj()
# self.reset_new_obj()
# self.vis_objects = []