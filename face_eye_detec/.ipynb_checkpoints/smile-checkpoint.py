from jetbot import Camera
from jetbot import bgr8_to_jpeg
from jetbot import Robot
import traitlets
#import ipywidgets.widgets as widgets
#from jetbot import Heartbeat
import cv2
import numpy as np
import os
#from IPython.display import display
import time
import subprocess


camera = Camera.instance(width=224, height=224)
#camera = Camera.instance()

#image = widgets.Image(format='jpeg', width=224, height=224)
#display(image)

#robot = Robot()
#robot.stop()


#face_cascade = 'C:\\Users\\vegar\\Desktop\\NTNU\\Elsys\\vaar20\\ImClasif\\clas\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
#eye_cascade = 'C:\\Users\\vegar\\Desktop\\NTNU\\Elsys\\vaar20\\ImClasif\\clas\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml'
#smile_cascade = 'C:\\Users\\vegar\\Desktop\\NTNU\\Elsys\\vaar20\\ImClasif\\clas\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml' 


face_seen = 1

face_haar_model = './data/haarcascade_frontalface_default.xml'
smile_haar_model = './data/haarcascade_smile.xml'
eye_haar_model = './data/haarcascade_eye.xml'
face = cv2.CascadeClassifier(face_haar_model)
smile = cv2.CascadeClassifier(smile_haar_model)
eye = cv2.CascadeClassifier(eye_haar_model)
#face = cv2.CascadeClassifier(face_cascade)
#smile = cv2.CascadeClassifier(smile_cascade)


def drive(faces):
    if robot.forward():
        eyes = eye.detectMultiScale(roi_gray, 1.8, 5)
        if ((eyes != ()) and (time.perf_counter()-time_start > 50)):
            robot.stop()
    else:
        robot.forward()
        time_start = time.perf_counter()
        


print('yesy')
print(type(face))
def detect(gray, frame):
    global face_seen
    print('2.1')
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face.detectMultiScale(gray, 1.3, 2)
    print('2.2')
    for (x, y, w, h) in faces: 

        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        print('2.3')
        #smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        eyes = eye.detectMultiScale(roi_gray, 1.8, 5)
        smiles = smile.detectMultiScale(roi_gray, 1.8, 5)
        print('2.4')
        if faces != ():
            if (face_seen != 1):
                
            
                print('its a face!')
            else:
                #subprocess.run(['play','./data/hello.mp3'])
                face_seen = 0
            #drive(faces)
        if smiles != ():
            
            print('Nice smile')
        if eyes != ():
            print('hi eyes')
        else:
            print('\n')
            
  
        for (sx, sy, sw, sh) in smiles: 
            print('2.5')
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            print('2.6')
            
        
        for (sx, sy, sw, sh) in eyes:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            
    return frame

#cap = cv2.VideoCapture(0)
while True:
    frame = camera.value
    #_, frame = cap.read()  
    print('1')
    print(frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('2')
    canvas = detect(gray, frame)
    print('3')
    cv2.imshow('Video', canvas)

    #camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        #robot.stop()
        break
    #cv2.imshow('Video', canvas)

    print('8')

camera.stop()
cv2.destroyAllWindows()
    # The control breaks once q key is pressed                         
    #if cv2.waitKey(1) & 0xff == ord('q'):                
        #break
#video_capture.release()                                  
#cv2.destroyAllWindows() 
#image = widgets.Image(format='jpeg', width=500, height=300) #making display image size width x height
#camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg) #merging the camera and the image, and transforming it to jpeg, bc display can only handle it
#display(image) #displaying the image in jupyter


    
    



#safety, if robor loosing connection
#def handle_heartbeat_status(change):
#    if change['new'] == Heartbeat.Status.dead:
#        camera_link.unlink()
#        robot.stop()

#heartbeat = Heartbeat(period=0.5)

# attach the callback function to heartbeat status
#heartbeat.observe(handle_heartbeat_status, names='status')

