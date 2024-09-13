# 영식 요금제 : 30초마다 10원
# 민식 요금제 : 60초마다 15원
# 3 <= 통화 횟수
# 40 40 40 <= 각 통화당 통화 시간
# M 45 <= 더 싼 요금제와 통화 요금
# Y M 50 <= 두개의 요금의 통화 총 금액이 같은 경우

# 통화 횟수 입력

# 각 통화에 대한 통화 시간 입력

# 통화 시간에 대한 리스트를 순회하면서 총 통화 시간 누적
# 민식과 영식 요금제에 대한 총 통화 요금을 누적하고 더 싼 것을 찾아야함
# 만약 같다면 Y M 으로 출력

while True:
    num = int(input(" 통화 횟수 입력 (<=20) : "))
    if 0 < num <= 20 :
        break
    else:
        print("잘못된 값의 통화 횟수를 입력했습니다. 다시 입력하세요.")
# while True:
#     time = list(map(int, input(" 통화 시간 입력 3개 (<=10000) : ").split() ))
#     for i in range(3):
#         if 0< time[i] <=10000 :
#             break
#         else:
#             print("잘못된 값의 통화 시간을 입력했습니다. 다시 입력하세요.")
#             break

time = list(map(int, input(" 통화 시간 입력 3개 (<=10000) : ").split() ))
print(time)
ys = 0
ms = 0

for i in range(num):
     x = (time[i]) // 30
     y = (time[i]) // 60

     ys += x * 10
     ms += y * 15

     x_m = (time[i]) % 30
     y_m = (time[i]) % 60

     if x_m != 0: ys += 10
     if y_m != 0: ms += 15

if ys > ms: print(f"M {ms}")
elif ys == ms: print(f"Y M {ys}")
else: print(f"Y {ys}")

# 리스트 입력 받을때 개수 num이랑 안맞으면 다시 입력받기
