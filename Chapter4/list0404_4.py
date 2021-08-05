#   1%のガチャの確率

import random

cnt_sum = 0
num_loop = int(input("繰り返し回数を入力:"))
num_rarechara = int(input("レアキャラの番号を入力(1～100):"))

for i in range(num_loop):
    cnt = 0
    while True:
        r = random.randint(1, 100)
        # print(r)
        cnt = cnt + 1
        if r == num_rarechara:  # <- 77番でレアキャラゲット
            break

    # print(str(cnt) + "回目でレアキャラをゲットぉぉぉぉぉ!!!")
    cnt_sum = cnt_sum + cnt

ave = cnt_sum / num_loop
print("繰り返し回数" + str(num_loop))
print("レアキャラゲットに要する平均回数= " + str(ave))
#   大体平均100回くらい -> 1%
