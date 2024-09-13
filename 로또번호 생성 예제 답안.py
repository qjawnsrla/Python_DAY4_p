import random

# 방법 1
print("로또 번호 자동 생성 : ", end = " ")
lotto = []
while len(lotto) <= 6:
    rand = random.randrange(1,46)   # 1 ~ 45
    if rand not in lotto:
        lotto.append(rand)
    if len(lotto) == 6: break
print(lotto)

# 방법 2
print("로또 번호 자동 생성 : ", end = " ")
lotto = set()
while len(lotto) <= 6:
    rand = random.randrange(1,46)
    lotto.add(rand)
print(lotto)