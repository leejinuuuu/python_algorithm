import math

t = int(input())

result = [0] * t

for _ in range(t):
    vals = list(map(int, input().split()))

    n = vals[0]

    for i in range(1, n+1):
        for j in range(1, i):
            result[_] = result[_] + math.gcd(vals[i], vals[j])

    print(result[_])