# cv2.resize(image, dsize, fx, fy, interpolation)
# - dsize: Manual Size
# - fx: 가로 비율
# - fy: 세로 비율
# - interpolation: 보간법
# INTER_CUBIC: 사이즈를 크게 할 때 주로 사용합니다.
# INTER_AREA: 사이즈를 작게 할 때 주로 사용합니다.
# 보간법은 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법을 의미합니다.

import cv2

image = cv2.imread('cat.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image', expand)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', shrink)
cv2.waitKey(0)
