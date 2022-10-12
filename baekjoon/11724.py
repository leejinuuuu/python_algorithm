import sys
sys.setrecursionlimit(10 ** 6)

# 참고 : https://fuzzysound.github.io/sys-setrecursionlimit

def dfs(v):
    visit_list[v] = 1        
    for i in range(1, n + 1):
        if visit_list[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())

visit_list = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)] 

connect_element = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

for i in range(1, n+1):
    if visit_list[i] == 0 :
        dfs(i)
        connect_element += 1

print(connect_element)