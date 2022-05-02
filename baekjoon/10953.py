import sys

T = int(input())
arr = []
for i in range(T):
    a, b = (map(int, sys.stdin.readline().split(',')))
    arr.append(a+b)

for i in range(T):
    print(arr[i])
