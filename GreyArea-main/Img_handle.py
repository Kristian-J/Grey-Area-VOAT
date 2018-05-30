
import cv2
from tkinter import *
from PIL import Image, ImageTk

class Imghandler():
    def __init__(self, origin):
        self.origin = origin
        self.local_frame = Frame(self.origin.disp_frame)

        self.image_name = 'temp.jpg'

        image = cv2.imread(self.image_name)

        # Rearrang the color channel
        b, g, r = cv2.split(image)
        img = cv2.merge((r, g, b))
        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(master = local_frame, image=im)

        # Put it in the display window
        label = Label(self.local_frame, image=imgtk)
        label.image = imgtk
        label.grid()
        # Label(self.local_frame, image=imgtk).grid()







        # image = Image.open("temp.jpg")
        # photo = ImageTk.PhotoImage(image)
        #
        # label = Label(image=photo)
        # label.image = photo # keep a reference!
        # label.grid()


        # img = cv2.imread('temp.jpg', 1)

        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
