
import cv2
from SaveData import *

class FeatureTrack:
    def __init__(self, cnt_img, fname, frame_num, objects, t_name):
        self.objects = objects
        self.t_name = t_name
        self.img = cv2.imread(cnt_img)
        self.file = fname
        self.cap = cv2.VideoCapture(self.file)
        self.frame_num = frame_num
        self.temp_objects = []
        # return
        # print("this is the feature handler data:", self.ojects,self.t_name,self.file,self.frame_num)

        img1 = cv2.imread('temp.jpg')  ##, cv2.IMREAD_GRAYSCALE)
        # print("&>>>>", self.frame_num, "<<<<&")
        self.cap.set(1, self.frame_num)
        ret, frame = self.cap.read()
        img2 = frame
        # img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # # img2 = cv2.imread('temp2.jpg', cv2.IMREAD_GRAYSCALE)
        # if t_name == 'Sift':
        #     # tracker = cv2.TrackerMIL_create()
        #     # tracker = cv2.xfeatures2d.SIFT_create()
        #     tracker = cv2.SIFT_create()
        # if t_name == 'Surf':
        #     tracker = cv2.xfeatures2d.SURF_create()
        # if t_name == 'Orb':
        #     tracker = cv2.ORB_create()
        #     # tracker = cv2.ORB_create(nfeatures=3000)
        print("c", t_name)
            # Create a tracker based on tracker name
        self.tracker_list = ["Boosting", "MIL", "KFC", "TLD", "MedianFlow", "GOTURN", "MOSSE", "CSRT"]
        #
        # if t_name == "Boosting":
        #     tracker = cv2.TrackerBoosting_create()
        # elif t_name == "MIL":
        #     tracker = cv2.TrackerMIL_create()
        # elif t_name == "KFC":
        #     tracker = cv2.TrackerKCF_create()
        # elif t_name == "TLD":
        #     tracker = cv2.TrackerTLD_create()
        # elif t_name == "MedianFlow":
        #     tracker = cv2.TrackerMedianFlow_create()
        # elif t_name == "GOTURN":
        #     tracker = cv2.TrackerGOTURN_create()
        # elif t_name == "MOSSE":
        #     tracker = cv2.TrackerMOSSE_create()
        # elif t_name == "CSRT":
        #     tracker = cv2.TrackerCSRT_create()

        multiTracker = cv2.MultiTracker_create()
        print(self.objects)
        for obj in self.objects:
            location = obj.obj_location[0],obj.obj_location[1],abs(obj.obj_location[0]- obj.obj_location[2]), abs(obj.obj_location[1]- obj.obj_location[3])

            ok = multiTracker.add(self.createTracker(self.t_name), img1, location)
            print("the location is: ", obj, location)
            # print("test one result is: ", ok)

        ok, BB = multiTracker.update(img2)
        if ok:
            for i, new_box in enumerate(BB):
                print('the multitracker result is :', i, new_box[0],new_box[1],new_box[2],new_box[3])
                ROI = int(new_box[0]), int(new_box[1]),int(new_box[0] + new_box[2]),int(new_box[1] + new_box[3])
                print("new coords are: ", ROI, "original location: ",self.objects[i].obj_location)
                # self.temp_objects.append(self.objects[i])
                # self.temp_objects[i].obj_location = ROI
                self.objects[i].obj_location = ROI
        else:
            print("object tracking error")
            return

        SaveToFile(self.objects, self.file, self.frame_num)


            # print("modified:", BB)
            # ROI = []
            # for i in BB:
            #     ROI.append(int(i))
            #
            # print("modified 2:", BB, ROI)
            # if ok:
            #     obj.obj_location = ROI
            #     self.temp_objects.append(obj)
            #     print(self.temp_objects)

        # SaveToFile(self.temp_objects, self.file, self.frame_num)
        # for i in self.temp_objects:
        #     print(i.obj_location)
            # cv2.imshow("image1", img2)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        return

    def createTracker(self, tracker_name):
        if tracker_name == self.tracker_list[0]:
            tracker = cv2.TrackerBoosting_create()
        elif tracker_name == self.tracker_list[1]:
            tracker = cv2.TrackerMIL_create()
        elif tracker_name == self.tracker_list[2]:
            tracker = cv2.TrackerKCF_create()
        elif tracker_name == self.tracker_list[3]:
            tracker = cv2.TrackerTLD_create()
        elif tracker_name == self.tracker_list[4]:
            tracker = cv2.TrackerMedianFlow_create()
        elif tracker_name == self.tracker_list[5]:
            tracker = cv2.TrackerGOTURN_create()
        elif tracker_name == self.tracker_list[6]:
            tracker = cv2.TrackerMOSSE_create()
        elif tracker_name == self.tracker_list[7]:
            tracker = cv2.TrackerCSRT_create()
        else:
            tracker = None
            print("traker designation not valid")

        return tracker

# # kp = sift.detect(img, None)
# keypoints, destcriptors = tracker.detectAndCompute(img1, None)
# img1 = cv2.drawKeypoints(img1, keypoints, None)
#
# keypoints, destcriptors = tracker.detectAndCompute(img2, None)
# img2 = cv2.drawKeypoints(img2, keypoints, None)
#
# # cv2.imshow("image1", frame)
# cv2.imshow("image1", img1)
# cv2.imshow("image2", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()