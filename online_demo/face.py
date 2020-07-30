from jetbot import Camera
from jetbot import bgr8_to_jpeg
from jetbot import Robot
import traitlets
import cv2
import numpy as np
import os

import time
import subprocess







        



def detect(gray, frame, face_seen):
    global face
    global smile
    global eye


    faces = face.detectMultiScale(gray, 1.3, 2)

    for (x, y, w, h) in faces: 

        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 

        eyes = eye.detectMultiScale(roi_gray, 1.8, 5)
        smiles = smile.detectMultiScale(roi_gray, 1.8, 5)

        if faces != ():
            if (face_seen != 1):
                
                print('its a face!')
            else:

                face_seen = 0
 
        if smiles != ():
            
            print('Nice smile')
        if eyes != ():
            print('hi eyes')
        else:
            print('\n')
            
  
        for (sx, sy, sw, sh) in smiles: 

            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
 
            
        
        for (sx, sy, sw, sh) in eyes:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            
    return frame





def face_main():
	global face
	global smile
	global eye

	camera_0 = Camera.instance(width=224, height=224)
	face_seen = 1
	face_haar_model = './data/haarcascade_frontalface_default.xml'
	smile_haar_model = './data/haarcascade_smile.xml'
	eye_haar_model = './data/haarcascade_eye.xml'
	face = cv2.CascadeClassifier(face_haar_model)
	smile = cv2.CascadeClassifier(smile_haar_model)
	eye = cv2.CascadeClassifier(eye_haar_model)
	while True:
		frame_0 = camera_0.value
		gray_0 = cv2.cvtColor(frame_0, cv2.COLOR_BGR2GRAY)
		canvas_0 = detect(gray_0, frame_0,face_seen)
		#cv2.imshow('Video', canvas_0)
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
	

	camera_0.stop()

	cv2.destroyAllWindows()


