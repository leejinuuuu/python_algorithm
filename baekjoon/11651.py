import sys

N = int(input())

L = []
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

L.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(str(L[i][0]) + " " + str(L[i][1]))
