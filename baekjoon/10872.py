import sys

N = int(sys.stdin.readline())
result = 1
for _ in range(N, 0, -1):
    result *= _

print(result)