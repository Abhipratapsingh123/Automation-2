import cv2
import numpy as np

foreground = cv2.imread('Segment-8/Images/giraffe.jpeg')
background = cv2.imread('Segment-8/Images/safari.jpeg')

width = foreground.shape[1]
height = foreground.shape[0]

resized_background = cv2.resize(background,(width,height))

for i in range(width):
  for j in range(height):
     pixel = foreground[j,i]
     if np.any(pixel == [1,255,0]):
       foreground[j,i] = resized_background[j,i]

cv2.imwrite('Segment-8/Images/background_changed.jpeg',foreground)