from posixpath import split
import sys


s = int(input())
arr = []
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
