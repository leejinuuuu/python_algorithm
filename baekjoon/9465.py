# from ctypes import sizeof
# import sys

# T = int(input())
# R = []
# for i in range(T):
#     N = int(input())

#     s = (list(map(int, sys.stdin.readline().split())))
#     s += (list(map(int, sys.stdin.readline().split())))

#     pos = 0
#     val = 0

#     for k in range(len(s)):
#         max = 0
#         for j in range(0, len(s)):
#             if s[j] > max:
#                 max = s[j]
#                 pos = j
#         val += s[pos]

#         s[pos] = 0

#         if int((pos - 1) % N) >= 0:
#             s[pos-1] = 0
#         if int((pos + 1) % N) != 0:
#             s[pos+1] = 0
#         if (pos + N) < len(s):
#             s[pos+N] = 0
#         if (pos - N) >= 0:
#             s[pos-N] = 0

#     R.append(val)

# for i in range(0, len(R)):
#     print(R[i])

t = int(input())
for i in range(t):
    s = []
    n = int(input())
    for k in range(2):
        s.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j - 1]
            s[1][j] += s[0][j - 1]
        else:
            s[0][j] += max(s[1][j - 1], s[1][j - 2])
            s[1][j] += max(s[0][j - 1], s[0][j - 2])
    print(max(s[0][n - 1], s[1][n - 1]))

    # 참고 : https://pacific-ocean.tistory.com/197
