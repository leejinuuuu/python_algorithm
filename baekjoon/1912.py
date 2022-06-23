N = int(input())
S = list(map(int, input().split()))

DP = [0]*N
DP[0] = S[0]

for i in range(1, N):
    DP[i] = max(S[i], DP[i-1]+S[i])

print(max(DP))
