import sys

n = int(input())
list = list(map(int, sys.stdin.readline().split()))

item = max(list)
sum = 0
for i in range(0, len(list)):
    sum += (list[i]/item)*100

print(str(sum/n))
