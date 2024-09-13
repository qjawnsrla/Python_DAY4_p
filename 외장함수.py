# 외장함수는 import해서 사용하는 함수, 파이썬에서 기본적으로 제공하는 것
# 랜덤 함수 : 지정한 범위 내에세 임의의 숫자를 만들어 내는 것
import random

for i in range(10):
    rand = random.randint(0, 4)  # 0 ~ 4이하 까지의 임의의 값을 생성
    print(rand, end=" ")
print()

for i in range(10):
    rand = random.randrange(0, 10)  # 0 ~ 10미만 까지의 임의의 값을 생성
    print(rand, end=" ")
print()
