import sys

A,B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

A_val = 0

for i in range(m):
    A_val += numbers[i]*(A**(m-1-i))

B_val = []

while A_val:
    B_val.insert(0, str(A_val%B))
    A_val = A_val//B

print(' '.join(B_val))