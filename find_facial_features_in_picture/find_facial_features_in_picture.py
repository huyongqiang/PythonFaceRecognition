# -*- coding: utf-8 -*-
# �Զ�ʶ����������
# filename : find_facial_features_in_picture.py

# ����pilģ�� ���������װ apt-get install python-Imaging
from PIL import Image, ImageDraw
# ����face_recogntionģ�飬�������װ pip install face_recognition
import face_recognition

# ��jpg�ļ����ص�numpy ������
image = face_recognition.load_image_file("jilingcheng.jpg")

#����ͼ���������沿�������沿����
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

for face_landmarks in face_landmarks_list:

   #��ӡ��ͼ����ÿ���沿������λ��
    facial_features = [
        'chin',
        'left_eyebrow',
        'right_eyebrow',
        'nose_bridge',
        'nose_tip',
        'left_eye',
        'right_eye',
        'top_lip',
        'bottom_lip'
    ]

    for facial_feature in facial_features:
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

   #��������ͼ��������ÿ������������
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for facial_feature in facial_features:
        d.line(face_landmarks[facial_feature], width=5)

    pil_image.show() 