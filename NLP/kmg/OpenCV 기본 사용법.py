#  cv2.imread(file_name, flag) = 이미지를 읽어 Numpy 객체로 만드는 함수
# - file_name: 읽고자 하는 이미지 파일
# - flag: 이미지를 읽는 방법 설정
# IMREAD_COLOR: 이미지를 Color 로 읽고, 투명한 부분은 무시
# IMREAD_GRAYSCALE: 이미지를 Grayscale 로 읽기
# IMREAD_UNCHANGED: 이미지를 Color로 읽고, 투명한 부분도 읽기(Alpha)
# 반환 값: Numpy 객체 (행, 열, 색상: 기본 BGR)

# cv2.imshow(title, image) = 특정한 이미지를 화면에 출력한다.
# - title: 윈도우 창의 제목
# - image: 출력할 이미지 객체

# cv2.imwrite(file_name, image) = 특정한 이미지를 파일로 저장하는 함수
# - file_name: 저장할 이미지 파일 이름
# - image: 저장할 이미지 객체

# cv2.waitKey(time) = 키보드 입력을 처리하는 함수
# - time: 입력 대기 시간 (무한대기: 0)
# 반환값: 사용자가 입력한 Ascii Code (ESC: 27)

# cv2.destroyAllWindow() = 화면의 모든 윈도우를 닫는 함수

import cv2

img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)  # 컬러
cv2.imshow('Image Basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png', img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)  # 흑백
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)
