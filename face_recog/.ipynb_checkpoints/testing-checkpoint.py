import cv2
import os

for files in os.listdir('./known_faces'):
    print(files)
    for file in os.listdir(f'./known_faces/{files}'):
        if(file == '.ipynb_checkpoints'):
            pass
        else:
            
            print(file)
#img = cv2. imread( './known_faces/Vegard/img/')
#cv2. imshow( 'sample image', img)
#cv2. waitKey( 0) # waits until a key is pressed.
#cv2. destroyAllWindows()