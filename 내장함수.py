# 내장함수 : 원래 제공되는 것, import 필요 없음
from audioop import reverse

from numba.cpython.randomimpl import rnd_state_ptr_t
from numexpr.expressions import div_op

# 매개변수로 전달된 값 중 가장 큰 값을 반환

print(max(32, 45, 67, 12, 45))
score = list(map(int, input("정수 입력 : ").split() ))  # 리스트 형으로 정수 값 반환
print(max(score))
print(max([1,2,3,4,5,6,7,8]))

print(min(32, 45, 67, 12, 45))
score = list(map(int, input("정수 입력 : ").split() ))  # 리스트 형으로 정수 값 반환
print(min(score))
print(min([1,2,3,4,5,6,7,8]))

# 시퀀스 자료형의 값을 모두 더해줌
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4]) / 5)

# 몫과 나머지를 반환, 튜플 형태로 반환(unpacking)
print(divmod(sum([1,2,3,4,5]), 5))  # 출력 결과 : (3, 0)  - 소괄호이므로 튜플

# 정렬
my_list = [1,5,77,99,23,345,23,555]
print(sorted(my_list))  # 오름차순 정렬
print(sorted(my_list, reverse = True))  # 내림차순 정렬
print(len(my_list))     # 요소의 개수를 구하는 함수이므로 출력결과 : 8


