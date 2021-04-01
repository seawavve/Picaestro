# OpenCV 이미지 합치기
# 이미지를 합치는 두 가지 방법
# 1. cv2.add(): Saturation 연산을 수항핸다.
# 0보다 작으면 0, 255보다 크면 255로 표현
# 2. np.add(): Modulo 연산을 수항핸다
# 256은 0, 257은 1로 표현

# 사진을 합치는 부분에 있어서 2가지 방법을 이용하였다.
# 1. cv.add()를 이용해 Saturation 연산을 이용하는 방법
# 2. 단순히 사진을 더하기 연산자를 이용해 사진을 합치는 방법
import cv2

image_1 = cv2.imread('couple.jpg')  # 사진을 불러오기 위한 작업
image_1 = cv2.resize(image_1, (500, 500))  # 사진을 합치기 위해 작업을 하기 위해서는 사진의 크기를 미리 정학는 작업이 필요하다.

image_2 = cv2.imread('flower.jpg')
image_2 = cv2.resize(image_2, (500, 500))

result = cv2.add(image_1, image_2)  # saturation 작업을 수행해서 원하는 방향으로 사진이 조화를 어울리면서 출력되었지만 사진마다 조화를 맞추는 부분에 있어서 한계가 있었다.
cv2.imshow('Image', result)
cv2.waitKey(0)

result = image_1 + image_2   # add 함수를 이용해 사진을 단순하게 합쳐보았지만 원하는 방향의 사진을 얻기는 어려웠다.
cv2.imshow('Image', result)
cv2.waitKey(0)
