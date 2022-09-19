import sys

n,b = map(str,sys.stdin.readline().split())

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0

n_list = list(n)
for i in range(len(n_list)):
    answer += int(tmp.index(n_list[len(n_list) - i - 1]) * (int(b) ** i))

print(str(answer))