import sys

c = int(input())
result = []

for i in range(c):
    values = (list(map(int, sys.stdin.readline().split())))
    avg = 0

    sum = 0
    for j in range(1, len(values)):
        sum += values[j]

    avg = (sum/values[0])

    num = 0
    for j in range(1, len(values)):
        if values[j] > avg:
            num += 1

    result.append(str(format(((num/values[0])*100), ".3f")) + "%")


for i in range(0, len(result)):
    print(result[i])
