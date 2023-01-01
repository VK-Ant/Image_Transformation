import cv2
import numpy as np

#Read
img = cv2.imread('5.jpg')
height,width = img.shape[:2]

#scale (resize)
img_scale = cv2.resize(img, None, fx=1.5,fy=1.5, interpolation = cv2.INTER_CUBIC)
cv2.imwrite("scale.png",img_scale)

#shear or skew (horizontal only)

M_shear = np.float32(
    [[1,0.5,0],
    [0,1,0]]
)

print("Shear matrix:", M_shear)
img_shear = cv2.warpAffine(img, M_shear,(int(width + 0.5*height),height))
cv2.imwrite("shear.png",img_shear)