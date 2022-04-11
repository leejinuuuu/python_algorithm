import sys

n = int(input())
list = []
for i in range(n):
    sum = 0
    s = str(input())
    o = 0
    for j in range(0, len(s)):
        if s[j] == "O":
            o += 1
        else:
            o = 0
        sum += o
    list.append(sum)

for i in range(0, len(list)):
    print(list[i])
