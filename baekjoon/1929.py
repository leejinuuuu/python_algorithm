import sys

def is_prime_number(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return False
    return True

# 참고 : https://deokkk9.tistory.com/17

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if is_prime_number(i):
        print(i)

