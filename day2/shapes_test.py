import cv2;
import numpy as np

## generate image
image=np.zeros((512,512,3),np.uint8) # black image
print(image.shape) # prints the dimensions of the image (height, width, channels) 

image[:]=255,120,230 # blue image

## create line
cv2.line(image,(50,50),(250,350),(255,0,0),3) # line from (0,0) to (300,300) with color blue and thickness 3

cv2.rectangle(image,(100,100),(300,300),(0,255,0),2) # rectangle from (100,100) to (300,300) with color green and thickness 2

cv2.circle(image,(400,400),50,(0,0,255),-1) # circle with center (400,400) and radius 50 with color red and filled

cv2.putText(image,'OpenCV',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2) # text 'OpenCV' at (200,200) with font size 1 and color yellow and thickness 2

cv2.imshow('blue image',image)
cv2.waitKey(0)