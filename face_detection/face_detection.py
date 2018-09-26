# -*- coding: utf-8 -*-
# 

# �������
import face_recognition
import cv2
import time

timeStart = time.clock()


# ��ȡͼƬ��ʶ������
img = face_recognition.load_image_file("jilingcheng.jpg")
face_locations = face_recognition.face_locations(img)
print face_locations

time_1 = time.clock()
timeRec = time_1 - timeStart
print("ʶ��ʱ�䣺",timeRec)

# ����opencv������ʾͼƬ
img = cv2.imread("jilingcheng.jpg")
cv2.namedWindow("ԭͼ")
cv2.imshow("ԭͼ", img)

# ����ÿ������������ע
faceNum = len(face_locations)
for i in range(0, faceNum):
    top =  face_locations[i][0]
    right =  face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]

    start = (left, top)
    end = (right, bottom)

    color = (55,255,155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

# ��ʾʶ����
cv2.namedWindow("ʶ��")
cv2.imshow("ʶ��", img)

cv2.waitKey(0)
cv2.destroyAllWindows()