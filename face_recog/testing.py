import cv2
import os
from jetbot import Camera

cam = Camera.instance()
#cam = cv2.VideoCapture(0)

while True:
	#ret, image = cam.read()
	cv2.imshow('Video', cam.value)

	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

cam.release()

#img = cv2. imread( './known_faces/Vegard/img/')
#cv2. imshow( 'sample image', img)
#cv2. waitKey( 0) # waits until a key is pressed.
cv2.destroyAllWindows()

'''
for files in os.listdir('./known_faces'):
    print(files)
    for file in os.listdir(f'./known_faces/{files}'):
        if(file == '.ipynb_checkpoints'):
            pass
        else:
          
            print(file)
'''
