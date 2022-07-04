T = int(input())

DP = [0]*101

DP[1] = 1
DP[2] = 1
DP[3] = 1
DP[4] = 2
DP[5] = 2
DP[6] = 3
DP[7] = 4
DP[8] = 5

R = []

for i in range(9, 101):
    DP[i] = DP[i-5] + DP[i-1]

for i in range(T):
    N = int(input())
    R.append(DP[N])

for i in range(T):
    print(R[i])

# ---------------------------------
# wh = [0 for i in range(101)]
# wh[1] = 1
# wh[2] = 1
# wh[3] = 1
# for i in range(0, 98):
#     wh[i + 3] = wh[i] + wh[i + 1]
# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(wh[n])
# 참고 : https://pacific-ocean.tistory.com/145
