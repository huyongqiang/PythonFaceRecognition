# -*- coding: utf-8 -*-
# ʶ�������������ĸ���

# ����face_recogntionģ�飬�������װ pip install face_recognition
import face_recognition
import numpy as np

#��jpg�ļ����ص�numpy������
mayun_image = face_recognition.load_image_file("mayun.jpg")
#Ҫʶ���ͼƬ
unknown_image = face_recognition.load_image_file("mayunz.jpg")

#��ȡÿ��ͼ���ļ���ÿ���沿���沿����
#����ÿ��ͼ���п����ж���棬���Է���һ�������б�
#����������֪��ÿ��ͼ��ֻ��һ��������ֻ����ÿ��ͼ���еĵ�һ�����룬������ȡ����0��
chen_face_encoding = face_recognition.face_encodings(mayun_image)[0]

known_faces = [
    chen_face_encoding
]

print("chen_face_encoding:{}".format(chen_face_encoding))
print("unknown_image size:{}".format(len(face_recognition.face_encodings(unknown_image))))
resultsArray = []
for index in range(len(face_recognition.face_encodings(unknown_image))):
     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[index]
     print("unknown_face_encoding:{}".format(face_recognition.face_encodings(unknown_image)[index]))
	 #�����True/false�����飬δ֪���known_faces�����е��κ�����ƥ��Ľ��
     results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
print("result :{}".format(results))
print("������� ���ưְ� ��? {}".format(results[0]))