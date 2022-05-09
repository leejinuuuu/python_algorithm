import sys

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = map(int, sys.stdin.readline().split(" "))

sum = 0
for i in range(1, m):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum += 31
    elif i == 2:
        sum += 28
    else:
        sum += 30
sum += d

print(day[sum % 7])
