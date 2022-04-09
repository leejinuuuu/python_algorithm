from posixpath import split
import sys


s = int(input())
arr = []
for i in range(s):
    str = input()
    A = int(str.split()[0])
    B = int(str.split()[1])
    arr.append(A+B)


for i in range(0, len(arr)):
    print(arr[i])
