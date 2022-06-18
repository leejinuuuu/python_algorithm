N = int(input())
A = list(map(int, input().split()))

DP = [0]*N
DP[0] = A[0]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + A[i])
        else:
            DP[i] = max(DP[i], A[i])

print(max(DP))
