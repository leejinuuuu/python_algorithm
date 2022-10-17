import sys
sys.setrecursionlimit(10**7)

T = int(sys.stdin.readline())

def dfs(n):
    visit_list[n]=1
    next = int(graph[n])
    if visit_list[next]==0:
        dfs(next)

for _ in range(T):
    answer=0

    N = int(sys.stdin.readline())
    
    visit_list = [0] * (N+1)
    graph = [0] + list(sys.stdin.readline().split())

    for i in range(1, N+1):
        if visit_list[i]==0:
            dfs(i)
            answer+=1

    print(answer)