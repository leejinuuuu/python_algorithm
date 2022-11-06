import sys
sys.setrecursionlimit(111111)

result_list = []

while True:
    w,h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = []

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]

    def DFS(x,y):
        if x<0 or x>=h or y<0 or y>=w:
            return False

        if(graph[x][y] == 1):
            graph[x][y]=0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                DFS(nx,ny)
            return True
        return False
        
    result = 0

    for i in range(h):
        for j in range(w):
            if DFS(i, j) == True:
                result += 1
    
    result_list.append(str(result))

print('\n'.join(result_list))