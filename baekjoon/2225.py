N, K = map(int, input().split())

DP = [[0]*201 for i in range(201)]

for i in range(1, 201):
    for j in range(1, 201):
        if i == 1:
            DP[i][j] = 1
        elif j == 1:
            DP[i][j] = DP[i-1][j]+1
        else:
            DP[i][j] = DP[i][j-1] + DP[i-1][j]

print(DP[K][N] % 1000000000)
