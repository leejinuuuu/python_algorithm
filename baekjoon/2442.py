# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(" ", end="")
#     for j in range(i*2 - 1):
#         print("*", end="")
#     print()

n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*'*((2*i)-1))
