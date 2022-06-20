N = int(input())
S = list(map(int, input().split()))
DP = [1]*N

for i in range(N):
    for j in range(i):
        if S[i] < S[j]:
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP))
