N = int(input())
# 10
S = list(map(int, input().split()))
# 1 5 2 1 4 3 4 5 2 1
S_R = S[::-1]
# 1 2 5 4 3 4 1 2 5 1

DP = [1]*N
DP_R = [1]*N

for i in range(N):
    for j in range(i):
        if S[i] > S[j]:
            DP[i] = max(DP[i], DP[j]+1)
            # 1 2 3 4 5
        if S_R[i] > S_R[j]:
            DP_R[i] = max(DP_R[i], DP_R[j]+1)
            # 1 2 5

result = [0]*N
for i in range(N):
    result[i] = DP[i] + DP_R[N-i-1] - 1

# print(DP)
# print(DP_R)

print(max(result))

# 참고 : https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
