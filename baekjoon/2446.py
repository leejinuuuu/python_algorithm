N = int(input())
for i in range(0, N):
    print(' '*i + '*'*(2*(N-i) - 1))
for i in range(N-2, -1, -1):
    print(' '*i + '*'*(2*(N-i) - 1))
