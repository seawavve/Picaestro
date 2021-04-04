# ROI 추출 및 복사

import cv2

image = cv2.imread('result1.png')

# Numpy Slicing: ROI 처리 가능
roi = image[200:350, 50:200]
cv2.imshow('Image', roi)
cv2.waitKey(0)

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi
cv2.imshow('Image', image)
cv2.waitKey(0)

