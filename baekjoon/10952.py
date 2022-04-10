import sys

list = []
while(True):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

    if a == 0 and b == 0:
        break


for i in range(0, len(list)-1):
    print(str(list[i]))
