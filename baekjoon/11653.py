import sys

N = int(sys.stdin.readline())

start = 2

while True:
    if N%start == 0:
        N = N//start
        print(str(start))
        start = 2
    else:
        start += 1
        if start > N:
            break