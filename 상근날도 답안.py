# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트메뉴 가격 = 햄버거 3개 중 제일 싼거 + 음료 2개 중 싼거 -50
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

# 방법 1
ls = list(map(int, input("입력 : ").split() ))
min_burger = min(ls[:3])
min_drink = min(ls[3:5])
print(f"세트 가격 : {min_burger + min_drink - 50}")

# 방법 2
# 만약 위처럼 문법이 생각이 안나고 선언부터 하는 경우 초기 기준값을 정해주어야 한다
ls = list(map(int, input("입력 : ").split() ))
min_burger = ls[0]
min_drink = ls[3]

for i in range(len(ls)):
    if i < 3 and min_burger > ls[i]:
        min_burger = ls[i]
    if i > 2 and min_drink > ls[i]:
        min_drink = ls[i]
print(f"세트 가격: {min_burger + min_drink - 50}")