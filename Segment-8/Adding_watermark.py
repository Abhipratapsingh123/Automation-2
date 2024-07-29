import cv2


# Load the two images
image = cv2.imread('Segment-8/Images/elfs.jpeg')
w_image = cv2.imread('Segment-8/Images/watermark.png')

print(image.shape)
print(w_image.shape)

x = image.shape[1]-w_image.shape[1]
y= image.shape[0]-w_image.shape[0]

watermark_place = image[y:,x:]
cv2.imwrite('Segment-8/Images/watermark_place.jpeg',watermark_place)

# creating the watermark
blend = cv2.addWeighted(watermark_place,0.5,w_image,0.5,0)
cv2.imwrite('Segment-8/Images/blend.jpeg',blend)

# adding back to image

image[y:,x:] = blend

cv2.imwrite('Segment-8/Images/elfs-watermarked.jpeg',image)




