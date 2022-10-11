# def dfs_recursive(graph, start, visited = []):
# ## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
#     visited.append(start)

#     for node in graph[start]:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)
#     return visited

# # 참고 : https://data-marketing-bk.tistory.com/44

# # BFS 메서드 정의
# def bfs (graph, node, visited):
#     from collections import deque
#     # 큐 구현을 위한 deque 라이브러리 활용
#     queue = deque([node])
#     # 현재 노드를 방문 처리
#     visited[int(node)] = True
    
#     # 큐가 완전히 빌 때까지 반복
#     while queue:
#         # 큐에 삽입된 순서대로 노드 하나 꺼내기
#         v = queue.popleft()
#         print(v, end=' ')
        
#         # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
#         for i in graph[v]:
#             if not (visited[int(i)]):
#                 queue.append(i)
#                 visited[int(i)] = True

# N, M, V = map(int, input().split())
# graph = dict()
# for i in range(int(M)):
#     A, B = map(str, input().split())
#     if(A in graph) :
#         tmp = graph.get(A)
#         if A < B:
#             tmp.append(B)
#         else:
#             tmp.insert(0, B)
        
#         graph[A] = tmp
#     else:
#         graph[A] = [B]

#     if B in graph:
#         tmp = graph.get(B)
#         if A < B:
#             tmp.append(B)
#         else:
#             tmp.insert(0, B)

#         graph[B] = tmp
#     else:
#         graph[B] = [A]
        
# graph = dict(sorted(graph.items()))

# visited = [False]*(N+1)

# print(*dfs_recursive(graph, str(V)))
# bfs(graph, str(V), visited)

# # MY CODE ERROR...

from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)