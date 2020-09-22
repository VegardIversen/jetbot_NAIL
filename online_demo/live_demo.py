import torch
import torchvision
import cv2
import numpy as np
from jetbot import Camera, bgr8_to_jpeg
from jetbot import Robot
import torch.nn.functional as F
import time


def preprocess(camera_value):
    global device, normalize
    x = camera_value
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    x = x.transpose((2, 0, 1))
    x = torch.from_numpy(x).float()
    x = normalize(x)
    x = x.to(device)
    x = x[None, ...]
    return x



def update(change):
    global blocked_slider, robot
    x = change['new'] 
    x = preprocess(x)
    y = model(x)
    

    y = F.softmax(y, dim=1)
    
    prob_blocked = float(y.flatten()[0])
    
    #blocked_slider.value = prob_blocked
    print(prob_blocked)
    if prob_blocked < 0.5:
        robot.forward(0.4)
    else:
        robot.left(0.4)
    
    time.sleep(0.001)

def collision_avoidance():

	global normalize, device, model, mean, camera, robot
	i_frame = -1

	model = torchvision.models.alexnet(pretrained=False)
	model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, 2)
	model.load_state_dict(torch.load('best_model.pth'))
	device = torch.device('cuda')
	model = model.to(device)
	mean = 255.0 * np.array([0.485, 0.456, 0.406])
	stdev = 255.0 * np.array([0.229, 0.224, 0.225])
	camera = Camera.instance(width=224, height=224)
    

	normalize = torchvision.transforms.Normalize(mean, stdev)

	robot = Robot()
	robot.stop()
	now = time.time()
	stop_time = now + 120
	while time.time() < stop_time:
		i_frame += 1
		if i_frame % 2 == 0:
		
			update({'new': camera.value})  # we call the function once to intialize
		#cv2.imshow(camera.value)

	#camera.observe(update, names='value')
	robot.stop()
	camera.stop()

#collision_avoidance()
#robot = Robot()
#robot.stop()

