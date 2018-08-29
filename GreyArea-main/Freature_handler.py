
import cv2
from SaveData import *

class FeatureTrack:
    def __init__(self, cnt_img, fname, frame_num, objects, t_name):
        self.ojects = objects
        self.t_name = t_name
        self.img = cv2.imread(cnt_img)
        self.file = fname
        self.cap = cv2.VideoCapture(self.file)
        self.frame_num = frame_num
        self.temp_objects = []
        # return
        # print("this is the feature handler data:", self.ojects,self.t_name,self.file,self.frame_num)

        img1 = cv2.imread('temp.jpg', cv2.IMREAD_GRAYSCALE)
        # print("&>>>>", self.frame_num, "<<<<&")
        self.cap.set(1, self.frame_num)
        ret, frame = self.cap.read()
        img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # img2 = cv2.imread('temp2.jpg', cv2.IMREAD_GRAYSCALE)
        if t_name == 'Sift':
            tracker = cv2.TrackerMIL_create()
            # tracker = cv2.xfeatures2d.SIFT_create()
        if t_name == 'Surf':
            tracker = cv2.xfeatures2d.SURF_create()
        if t_name == 'Orb':
            tracker = cv2.ORB_create(nfeatures=3000)
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

        for obj in self.ojects:
            location = obj.obj_location
            print("the location is: ", location)

            ok = tracker.init(img1, location)
            # print("test one result is: ", ok)

            ok, BB = tracker.update(img2)
            print("modified:", BB)
            if ok:
                obj.obj_location = BB

            # cv2.imshow("image1", img2)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        return