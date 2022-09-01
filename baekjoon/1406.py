# S = list(input())

# cursor_index = len(S)

# for _ in range(int(input())):
#     command = list(input().split())

#     if(command[0] == "L" and cursor_index>0):
#         cursor_index = cursor_index - 1
#     elif(command[0] == "D" and cursor_index<len(S)):
#         cursor_index = cursor_index + 1
#     elif(command[0] == "B" and cursor_index > 0):
#         # S.pop(cursor_index)
#         S.remove(S[cursor_index-1])
#     else:
#         S.insert(cursor_index, command[1]) 
#         cursor_index = cursor_index + 1

# print("".join(S))
    
# 시간초과...

import sys

S = list(sys.stdin.readline().strip())
# 마지막의 엔터키를 입력받지않기 위한 strip()
S1 = []

for line in sys.stdin:
    if line[0] == "L":
        if S: S1.append(S.pop())
        else: continue
    elif line[0] == "D":
        if S1: S.append(S1.pop())
        else: continue
    elif line[0] == "B":
        if S: S.pop()
        else: continue
    elif line[0] == "P":
        S.append(line[2])

    print(S)
    print(S1)

print("".join(S+list(reversed(S1))))
# 참고 : https://bnzn2426.tistory.com/112