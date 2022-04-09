from posixpath import split
import sys

s = int(input())
arr = []

for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a+b)

for i in range(0, s):
    print("Case #"+str(i+1)+": "+str(arr[i]))
