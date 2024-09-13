# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트메뉴 가격 = 햄버거 3개 중 제일 싼거 + 음료 2개 중 싼거 -50
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

menu = list (map(int, input("햄버거 3개, 음료 2개 입력 : ").split() ))
hbr = []
dr = []
for e in range(len(menu)):
    if e<3: hbr.append(menu[e])
    else: dr.append(menu[e])
sett = int(min(hbr))+ int(min(dr)) - 50
print(f"세트 : {sett}원")