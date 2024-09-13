# 무작위의 수를 공백으로 기준하여 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제

n = list(map(int, input("무작위의 수 입력 : ").split() ))
n_odd = []
n_even = []
for num in n:
    if num%2 == 1:
        n_odd.append(num)
    else:
        n_even.append(num)
print(f"홀수 리스트 : {n_odd}")
print(f"짝수 리스트 : {n_even}")
