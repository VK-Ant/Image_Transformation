import cv2
import numpy as np

#Read
img = cv2.imread('5.jpg')
height,width = img.shape[:2]

#Affine transform (include translation, rotation, scale)
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M_off = cv2.getAffineTransform(pts1,pts2) #compute affine transformation

print("Computed affine transform matrix:", M_off)

img_off = cv2.warpAffine(img,M_off, (width,height))

cv2.imwrite("Affine_warp.png", img_off)