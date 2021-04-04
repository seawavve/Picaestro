# OpenCV를 활용한 특정 범위 픽셀 변경

import cv2
import time

image = cv2.imread('cat.jpg')

# 이 경우는 좀 오래걸림
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

# 이 경우가 좀 더 효율적임
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('Image', image)
cv2.waitKey(0)

