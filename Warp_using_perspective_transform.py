#Perspective transformation

import cv2
import numpy as np

#read image
img = cv2.imread('5.jpg')
height,width = img.shape[:2]

#perspective transform
pts1 = np.float32([[220,85],[223,414],[602,190],[616,323]])
pts2 = np.float32([[75,75],[75,225],[500,75],[500,225]])

M_persp = cv2.getPerspectiveTransform(pts1,pts2)

print("Computed perspective transform matrix:", M_persp)

img_persp = cv2.warpPerspective(img,M_persp,(600,300))
cv2.imwrite("perspective_transform.png", img_persp)