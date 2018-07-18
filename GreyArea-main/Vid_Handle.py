import cv2
import numpy as np
from tkinter import *
from tkinter import ttk


class VidHandler():
    def __init__(self, origin):
        self.origin = origin
        self.file = origin.cnt_vid
        self.cap = cv2.VideoCapture('vtest.avi')
        self.total_frames = self.cap.get(7)
        print('the numer of frames are: ', self.total_frames)
        self.frame_num = 0
        self.extract_frame(0)
        self.local_frame = Frame(self.origin.controls_frame)
        self.local_frame.grid(sticky = N)
        global f_input
        labelmsg = "Max frame #:  " + str(self.total_frames - 1)
        print(labelmsg)
        label = Label(self.local_frame, text=labelmsg)
        label.grid(row=0, column=0)
        f_input = Entry(self.local_frame, width=20 )
        f_input.grid(row=0, column=1)
        f_input.bind("<Return>", self.set_f_num)

        f_input_enter = Button(self.local_frame, text="Enter")
        f_input_enter.grid(row=0, column=2)
        f_input_enter.bind("<Button-1>", self.set_f_num)

    def set_f_num(self, event=NONE):
        global f_input
        frame_num = f_input.get()
        print('the frame number is: ', frame_num, type(frame_num))
        try:
            frame_num = int(frame_num)
        except:
            print('Imput was not a number')
            pass
        if type(frame_num) == int:
            if 0 <= frame_num < self.total_frames:
                self.extract_frame(frame_num)
            else: print("number out of range")
    def extract_frame(self, num):
            self.cap.set(1, num)
            ret, frame = self.cap.read()
            cv2.imwrite('temp.jpg', frame)
            self.origin.disp_img('temp.jpg')