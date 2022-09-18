# N, B = map(int, input().split())

# val = []

# while(True):
#     lit = N//B
#     rs = N-(lit*B)
#     val.insert(0, str(rs))
    
#     N = lit

#     if N<B:
#         val.insert(0, str(N))
#         break

# for _ in range(len(val)):
#     if int(val[_])>=10:
#         val[_] = chr(55+int(val[_]))

# print(''.join(val))

import sys

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())
answer = ''

while n != 0:
    answer += str(tmp[n % b])
    n = n // b

print(answer[::-1])

# 참고 : https://duwjdtn11.tistory.com/486