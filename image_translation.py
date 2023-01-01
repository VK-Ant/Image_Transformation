import cv2
import numpy as np

#read image
img = cv2.imread('5.jpg')
height,width = img.shape[:2]

cv2.imwrite('original.png',img)

#Translation
M_trans = np.float32(
    [[1,0, 100],
    [0,1,50]]
)
print("Translation Matrix: ")
print("M_Translation")

img_trans = cv2.warpAffine(img, M_trans,(width,height))
cv2.imwrite("Translation.png", img_trans)



