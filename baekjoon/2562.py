import sys

list = []
for i in range(9):
    list.append(int(input()))

max = 0
num = 0
for i in range(0, len(list)):
    if max <= list[i]:
        max = list[i]
        num = i+1

print(max)
print(num)
