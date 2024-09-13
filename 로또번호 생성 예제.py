# 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# 리스트를 사용하고, 리스트내에 임의로 생성한 번호가 있으면 추가하면 안된다
# 몇 번의 중복이 발생할지 알 수 없기 때문에 횟수가 정해지지 않은 반
import random

num = []
for i in range(6):
    rand = random.randint(0, 45)
    num.insert(i,rand)
    for j in range(i+1):
        if num[j] == num[i]:
            num[i] = num.insert(i,rand)
            break
        else:
            break
    print(i, end="")
print(num)
