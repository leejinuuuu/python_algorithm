import math

T=int(input())

result = []

for _ in range(T):
    A,B = map(int, input().split())
    result.append(math.lcm(A,B))

for _ in range(T):
    print(result[_])