import sys

list = []
while(True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        list.append(a+b)
    except:
        break

for i in range(0, len(list)):
    print(str(list[i]))
