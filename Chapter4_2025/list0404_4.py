import random

# cnt = 0
max_cnt = 1000
sum_cnt = 0
for i in range(max_cnt):
    cnt = 0
    while True:
        r = random.randint(1, 100)
        # print(r)
        cnt = cnt + 1
        if r == 77:
            sum_cnt = sum_cnt + cnt
            break
    # print(str(cnt) + "回目でレアキャラゲット!!")
avr = sum_cnt / max_cnt
print(avr)
