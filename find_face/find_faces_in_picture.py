# -*- coding: utf-8 -*-
#  ʶ��ͼƬ�е�������������ʾ����
# filename : find_faces_in_picture.py

# ����pilģ�� ���������װ apt-get install python-Imaging
from PIL import Image
# ����face_recogntionģ�飬�������װ pip install face_recognition
import face_recognition

# ��jpg�ļ����ص�numpy ������
image = face_recognition.load_image_file("mayunz.jpg")

# ʹ��Ĭ�ϵĸ���HOGģ�Ͳ���ͼ������������
# ��������Ѿ��൱׼ȷ�ˣ������ǲ���CNNģ����ô׼ȷ����Ϊû��ʹ��GPU����
# ����μ�: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

# ʹ��CNNģ��
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

# ��ӡ���Ҵ�ͼƬ���ҵ��� ���� ������
print("I found {} face(s) in this photograph.".format(len(face_locations)))

# ѭ���ҵ�����������
for face_location in face_locations:

        # ��ӡÿ������λ����Ϣ
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right)) 
# ָ��������λ����Ϣ��Ȼ����ʾ����ͼƬ
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show() 