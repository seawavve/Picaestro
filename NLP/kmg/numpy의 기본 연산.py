# numpy 의 기본 연산
# - numpy 는 배열에 대한 기본적인 사칙연산을 지원한다

import numpy as np

# numpy 간단한 연산
array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

result_array = array * 10
print(result_array)

# 서로 다른 형태의 numpy 연산
# - numpy 는 서로 다른 형태의 배열을 연산할 때는 행 우선으로 수행된다
array1 = np.arange(4).reshape(2, 2)  # (2 x 2) 형태
array2 = np.arange(2)  # (1 x 2) 형태

array3 = array1 + array2
print(array3)

# - 브로드캐스트: 형태가 다른 배열을 연산할 수 있도록 배열의 형태을 동적으로 변환
array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(0, 4).reshape(4, 1)  # (4 x 1)의 형태

print(array3 + array4)

# numpy 의 마스킹 연산
# - 마스킹: 각 원소에 대하여 체크한다.
array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10  # 10보다 작으면 True 크면 False
print(array2)

array1[array2] = 100  # True 의 값을 다 100으로 바꿔줌
print(array1)

# numpy 의 집계 함수
array = np.arange(16).reshape(4, 4)
print(array)
# 특정 array 값 이용
print("합계: ", np.sum(array, axis=0))  # 열에 대한 모든 행의 값을 던한 값

# 전체 array 값 이용
print("최대값:", np.max(array))
print("최소값:", np.min(array))
print("합계:", np.sum(array))
print("평균값", np.mean(array))
