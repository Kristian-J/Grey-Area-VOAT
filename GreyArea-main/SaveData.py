
import os
from Visual_object import *


class SaveToFile:
    def __init__(self, vis_objects, fname, frame_num):
        self.fname = fname
        self.objects = vis_objects
        self.frame_num = frame_num
        self.save_file = None
        # print("objects:  ",self.objects)
        self.file = set_file_name(self.fname, self.frame_num)
        # print("filename is :", self.file)

        self.text = self.make_text(self.objects)
        print("file text is : \n", self.text)

        f = open(self.file, "w+")
        f.write(self.text)
        f.close()

    def make_text(self, vis_obs):
        index = 0
        temp = str("")
        for ob in vis_obs:
            temp += str(index) + "," + str(ob.obj_location[0]) + "," + str(ob.obj_location[1]) + "," + str(ob.obj_location[2]) + "," + str(ob.obj_location[3])
            tag = ob.obj_tag
            print(tag)
            temp = temp + "," + str(tag)
            # temp += str(tags[-1])
            temp += str("\n")
            index += 1
        return temp


def set_file_name(fname, num):
    x = fname.split('.')
    y = ""
    if num is not None:
        y += str(x[0]) + "." + str(num) + ".txt"
    else:
        y = str(x[0] + ".txt")
    # print(x, y)
    return y
    pass


class LoadData:
    """this class is for loading annotated visual object data"""
    """input is the current file name, frame number if applicable, and the tkinter frame that will host the object"""
    def __init__(self, fname, num, host_frame):
        self.file = None
        self.fname = fname
        self.frame_num = num
        self.host_frame = host_frame
        self.temp_coords = []
        self.temp_tag = None
        self.temp_obj = None
        self.image_objects = []
        self.load = False
        self.file = set_file_name(self.fname, self.frame_num)
        if os.path.isfile(self.file):
            try:
                rawdata = open(self.file)
                self.load = True
            except:
                return
            for line in rawdata:
                line = line.rstrip("\n").split(',')
                self.temp_coords = [int(line[1]), int(line[2]), int(line[3]), int(line[4])]
                self.temp_tag = line[5]
                self.temp_obj = VisualObject(self.temp_coords, self.temp_tag, self.host_frame)
                self.image_objects.append(self.temp_obj)

                # print(self.image_objects)
                # print(self.temp_obj.host_frame, self.temp_obj.obj_location)