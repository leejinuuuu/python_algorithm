import sys

N = int(input())
student_list = []
for _ in range(N):
    name, korean, english, math = map(str, sys.stdin.readline().split())

    korean = int(korean)
    english = int(english)
    math = int(math)

    student_list.append((name, korean, english, math))

student_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(student_list[i][0])
