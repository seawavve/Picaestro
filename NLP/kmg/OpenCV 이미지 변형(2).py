# 이미지 위치 변경
# cv2.warpAffine(image, M, dsize)
# - M: 변환행렬
# - desize: Manual Size

import cv2
import numpy as np

image = cv2.imread('cat.jpg')

# 행과 열 정보만 저장한다.
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
