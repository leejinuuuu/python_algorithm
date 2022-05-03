import sys

for i in range(3):
    A, B = map(str, sys.stdin.readline().split(" "))
    a_h, a_m, a_s = map(int, A.split(":"))
    b_h, b_m, b_s = map(int, B.split(":"))

    count = 0
    while True:
        if a_s == 60:
            a_s = 0
            a_m += 1
        if a_m == 60:
            a_m = 0
            a_h += 1
        if a_h == 24:
            a_h = 0
            a_m = 0
            a_s = 0

        if (a_h*10000+a_m*100+a_s) % 3 == 0:
            count += 1
        if a_h == b_h and a_m == b_m and a_s == b_s:
            break

        a_s += 1
    print(count)
