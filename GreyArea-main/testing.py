import csv
import cv2
from SaveData import *
from tkinter import *



# SaveToFile([[204, 187, 324, 250, 'truck'],[250, 324, 187, 204, 'car']], "hopscotch.jpg", None)

# LoadData("C:/Users/Kriso/Pictures/Pictures/New folder (2)/r_soulcaliburgirls.txt", None, 'this is the frame name')


img = cv2.imread('temp.jpg', cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create(nfeatures=3000)

# kp = sift.detect(img, None)
keypoints, destcriptors = orb.detectAndCompute(img, None)
img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#
# class TestClass:
#     def __init__(self):
#
#         self.root = Tk()
#         self.menu_frame = Frame(self.root)
#         self.menu_frame.grid()
#         self.root.title("Welcome")
#
#         option_frame=Frame(self.menu_frame)
#         option_frame.grid(row=3, column = 1)
#         tracker_list = ['Sift', 'Surf', 'Orb']
#         self.selected_tracker=StringVar()
#         tracker_name = "Sift"
#         self.selected_tracker.set(tracker_name)
#         print('initial traker name is: ', self.selected_tracker.get())
#         tracker_menu = OptionMenu(option_frame, self.selected_tracker, 'Sift', 'Surf', 'Orb')
#         tracker_menu.config(width=10)
#         tracker_menu.grid(row = 1, column = 0)
#         thislabel = Label(option_frame, text = 'Tracker:')
#         thislabel.grid(row = 0, column = 0)
#         thislabel2 = Label(option_frame, textvariable = self.selected_tracker)
#         thislabel2.grid(row = 0, column = 1)
#         self.tracker_select = Button(option_frame, text = "set", command = self.set_tracker)
#         self.tracker_select.grid(row = 2, column = 0)
#
#         self.root.mainloop()
#     def set_tracker(self):
#         print('you have arrived')
#         return
#
# testing = TestClass()