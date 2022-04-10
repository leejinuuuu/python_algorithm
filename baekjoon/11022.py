from posixpath import split
import sys

s = int(input())
a = []
b = []
for i in range(s):
    fir, sen = map(int, sys.stdin.readline().split())
    a.append(fir)
    b.append(sen)

for i in range(0, s):
    print("Case #"+str(i+1)+": " +
          str(a[i]) + " + "+str(b[i])+" = "+str(int(a[i])+int(b[i])))
