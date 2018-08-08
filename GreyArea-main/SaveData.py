




class SaveToFile:

    def __init__(self, vis_objects, fname, frame_num):
        self.fname = fname
        self.objects = vis_objects
        self.frame_num = frame_num
        self.save_file = None
        print("objects:  ",self.objects)
        self.file = self.set_file_name(self.fname, self.frame_num)
        print("filename is :", self.file)

        self.text = self.make_text(self.objects)
        print("file text is : \n", self.text)

        f = open(self.file, "w+")
        f.write(self.text)
        f.close()


    def set_file_name(self, fname, num):
        x = fname.split('.')
        y = ""
        if self.frame_num is not None:
            y += str(x[0]) + "." + str(self.frame_num) + ".txt"
        else:
            y = str(x[0] + ".txt")
        # print(x, y)
        return y
        pass

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

