import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
total_frames = cap.get(7)

# print(total_frames)

cap.set(1, 200)
ret, frame = cap.read()
cv2.imwrite('temp.jpg', frame)

img = cv2.imread('temp.jpg', 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# cap = cv2.VideoCapture('vtest.avi')
#
# while True:
#     ret, frame = cap.read()
#
#
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
