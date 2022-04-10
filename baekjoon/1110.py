import sys

n = int(sys.stdin.readline())
s = 0
change_num = n
result = 0

while(True):
    s = 10*int(change_num % 10) + \
        int((int(change_num/10)+int(change_num % 10)) % 10)
    result += 1
    change_num = s

    if change_num != n:
        continue
    break


print(str(result))
