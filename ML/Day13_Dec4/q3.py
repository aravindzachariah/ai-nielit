import cv2
import numpy as np
img = cv2.imread('girl.jpg',0)
kernel = np.ones((2,2),np.uint8)
img1= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img1= cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
img=np.hstack((img,img1))
cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
