N = list(map(int, input()))
L = len(N)
DP = [0 for _ in range(L+1)]

if N[0] == 0:
    print("0")
else:
    N = [0] + N
    DP[0] = DP[1] = 1

    for i in range(2, L+1):
        if N[i] > 0:
            DP[i] += DP[i-1]
        temp = N[i-1] * 10 + N[i]
        if temp >= 10 and temp <= 26:
            DP[i] += DP[i-2]
    print(DP[L] % 1000000)

# 참고 : https://jyeonnyang2.tistory.com/55
