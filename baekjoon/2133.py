N = int(input())
DP = [0 for _ in range(31)]

DP[2] = 3
# DP[2]=3, DP[4]=11, DP[6]=41

for i in range(4, 31, 2):
    # 홀수는 0

    DP[i] = DP[2]*DP[i-2]

    for j in range(4, i, 2):
        DP[i] += 2*DP[i-j]

    DP[i] += 2

print(DP[N])

# 참고 : https://www.notion.so/Mine-710e2bd2ae244f50a1cf4c3b9db97f47
