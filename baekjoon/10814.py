import sys

N = int(input())
people_list = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    people_list.append((age, name))

people_list.sort(key=lambda x: (x[0]))

for i in people_list:
    print(i[0], i[1])
