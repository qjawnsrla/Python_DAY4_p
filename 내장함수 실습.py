# 실습
from numba.cpython.randomimpl import rnd_state_ptr_t

n = list(map(int, input("정수 입력 : ").split() ))
# 입력받은 값에서 제일 큰 값
print(max(n))
print(f"최대값 : {max(n)}")
# 입력받은 값에서 제일 작은 값
print(min(n))
print(f"최소값 : {min(n)}")
# 총점
print(sum(n))
print(f"총점 : {sum(n)}")
# 평균
print(sum(n) / len(n))
print(f"평균 : {sum(n) / len(n)}")
# 해당 리스트(n)를 5로 나눈 몫과 나머지
for i in range(len(n)):
    print(divmod(n[i],len(n)), end="")
    if i < len(n)-1: print("," ,end="")

print(f"몫과 나머지 : {divmod(sum(n), 5)}")