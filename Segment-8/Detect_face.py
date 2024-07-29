import cv2


image = cv2.imread('Segment-8/Images/humans.jpeg',1)
face_cascade = cv2.CascadeClassifier('Segment-8/faces.xml')

faces = face_cascade.detectMultiScale(image,1.1,4)

for (x,y,w,h) in faces:
  cv2.rectangle(image,(x,y),(x+w ,y+h),(255,255,255),4)

cv2.imwrite('Segment-8/Images/humans_faces.jpeg',image)