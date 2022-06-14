# import sys


# N = int(input())
# s = list(map(int, sys.stdin.readline().split(" ")))
# max = 0
# length = 0
# for i in range(len(s)):
#     if max < s[i]:
#         max = s[i]
#         s[i] = 0
#         i = 0
#         length +=1

# print(length)

N = int(input())
s = list(map(int, input().split(" ")))
t = [1] * N

for i in range(N):
    for j in range(i):
        if s[i] > s[j]:
            t[i] = max(t[i], t[j]+1)


print(max(t))

# 참고 : https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%8011053%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-LIS-DP
