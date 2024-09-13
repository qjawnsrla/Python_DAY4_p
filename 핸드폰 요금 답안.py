cnt = int(input("통화 횟수 : "))
call_time = list(map(int, input("각 통화시간 : ").split() ))

y_pay = m_pay = 0
for i in range(cnt):
    y_pay += (call_time[i] // 30) * 10 + 10
    m_pay += (call_time[i] // 60) * 15 + 15

if y_pay > m_pay:
    print(f"M {m_pay}")
elif y_pay < m_pay:
    print(f"Y {y_pay}")
else:
    print(f"M Y {m_pay}")