import sys

n = int(input())

list = list(map(int, sys.stdin.readline().split()))

min = 10000001
max = -10000001

for i in range(0, len(list)):
    if min >= list[i]:
        min = list[i]
    if max <= list[i]:
        max = list[i]

print(str(min) + " " + str(max))
