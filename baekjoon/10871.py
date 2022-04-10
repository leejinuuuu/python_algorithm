import sys

n, x = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))

for i in range(0, len(list)):
    if list[i] < x:
        print(str(list[i]), end=" ")
