# 무작위의 수를 공백으로 기준하여 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제

# 방법 1
number = list (map(int, input("입력 : ").split() ))
even = []
odd = []

for e in number:
    if e%2 == 0: even.append(e)
    else: odd.append(e)
print(f"홀수 : {odd}")
print(f"짝수 : {even}")

# 방법 2 - 더 간결하게
number = list (map(int, input("입력 : ").split() ))
odd = list(filter(lambda x: x%2 == 1, number))      #filer 는 조건에 맞는 것을 골라주는 함수
even = list(filter(lambda x: x%2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")