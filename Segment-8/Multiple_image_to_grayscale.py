import cv2
import os

images = os.listdir('Segment-8/Images')

for image in images:
  gray = cv2.imread(f'Segment-8/Images/{image}',0)
  cv2.imwrite(f'Segment-8/Grayscale_images/{image}',gray)