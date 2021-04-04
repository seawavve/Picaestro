# OpenCV 를 활용한 픽셀별 색상 다루기

import cv2

image = cv2.imread('cat.jpg')
image[:, :, 2] = 0

cv2.imshow('Image', image)
cv2.waitKey(0)
