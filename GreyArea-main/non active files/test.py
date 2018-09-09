from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np



# A root window for displaying objects
root = Tk()
frame = Frame(root)
image_name = 'temp.jpg'

image = cv2.imread(image_name)

# Rearrang the color channel
b, g, r = cv2.split(image)
img = cv2.merge((r, g, b))
# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

# Put it in the display window
label = Label(frame, image=imgtk)
label.grid()

root.mainloop() # Start the GUI