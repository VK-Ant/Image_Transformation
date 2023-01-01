import cv2
import numpy as np

#read
img = cv2.imread("5.jpg")
height,width = img.shape[:2]

print("height:",height)
print("width:",width)

#Rotation
M_rot = cv2.getRotationMatrix2D((0,0),45,1) #45deg, scale = 1
print("Rotation matrix(around origin):", M_rot)

img_rot = cv2.warpAffine(img, M_rot,(width,height))

cv2.imwrite("rotation.png",img_rot)

#rotation around center (translation + rotation)
#Rotation
M_rot_center = cv2.getRotationMatrix2D((width/2,height/2),-45,1) #-45deg, scale = 1
print("Rotation matrix(around center):", M_rot_center)

img_rot_center = cv2.warpAffine(img, M_rot_center,(width,height))

cv2.imwrite("rotation_around_center.png",img_rot_center)
