from itertools import count
import sys


a = int(input())
b = int(input())
c = int(input())


mul = a*b*c

for i in range(0, 10):
    print(str(mul).count(str(i)))
