import cv2

image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽렐을 가리킨다
px = image[100, 100]

# B, G R 순서대로 출력된다
# (단, Gray Scale 인 경우에는 B, R, G로 구분되지 않은다.)
print(px)

# R 값만 출력하기
print(px[2])