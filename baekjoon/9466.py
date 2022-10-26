# import sys
# sys.setrecursionlimit(10 ** 6)

# T = int(sys.stdin.readline())

# result_list = []

# for _ in range(T):
#     n = int(sys.stdin.readline())
#     student_choice_number = list(map(int, sys.stdin.readline().split()))

#     count = 0

#     for i in range(n):
#         numbers = []
#         while True:

#             if i == student_choice_number[i] - 1:
#                 count += 1
#                 numbers = []
#                 break 
#             else:
#                 if student_choice_number[i] in numbers:
#                     break
#                 else:
#                     numbers.append(student_choice_number[i])

#                     i = student_choice_number[i] - 1

#     result_list.append(str(n-count))

# print("\n".join(result_list))

# 시간 에러...

import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수

# 참고 : https://claude-u.tistory.com/435