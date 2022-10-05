import sys
import math

N = math.factorial(int(sys.stdin.readline()))

result = list(str(N))
value = 0
for _ in range(len(result)-1, -1, -1):
    if result[_] != '0':
        print(str(value))
        break
    else:
        value += 1