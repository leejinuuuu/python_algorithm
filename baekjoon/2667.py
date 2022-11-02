n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우를 구현하기 위함
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count # 외부에서 선언된 count라는 함수를 global 변수로 재선언함으로써 접근가능해짐
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])

# 참고 : https://hongcoding.tistory.com/71