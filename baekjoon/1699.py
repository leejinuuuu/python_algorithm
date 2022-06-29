# N = int(input())
# r = int(N**(1/2))
# sum = 0
# count = 0
# while(True):
#     sum = sum + (r**2)
#     r = int((N-sum)**(1/2))
#     count += 1
#     if sum == N:
#         break
# print(str(count))

N = int(input())

DP = [x for x in range(N+1)]
for i in range(1, N+1):
    DP[i] = i
    for j in range(1, i):
        if(j**2) > i:
            break
        if DP[i] > DP[i-j**2]+1:
            DP[i] = DP[i-j**2]+1

print(DP[N])

# 참고 : https://jyeonnyang2.tistory.com/50
