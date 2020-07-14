import cv2
from jetbot import Camera

#todo: Add facedetection to check if someone in frame.
#possibilty: if unknown face add to known, need som way to write name. Mb with mic in usb camera. 

camera = Camera.instance()
i = 43 #for filename
while True:  
    frame = camera.value
    if cv2.waitKey(500) == ord('a'):
        filename = f'chessboard{i}.jpg'
        cv2.imwrite(f'./chessboard_img/{filename}', frame)
        i += 1
        print('saved picture')
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
camera.stop()
                                 
cv2.destroyAllWindows()