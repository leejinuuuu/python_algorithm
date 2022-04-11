import sys

list = []


for i in range(int(10)):
    list.append(int(int(input()) % 42))

list.sort()

count = 1
for i in range(1, len(list)):
    if list[i-1] != list[i]:
        count += 1

print(str(count))
