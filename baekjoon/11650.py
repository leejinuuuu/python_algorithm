import sys

N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

L.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(str(L[i][0]) + " " + str(L[i][1]))

# 참고 : https://haesoo9410.tistory.com/193
