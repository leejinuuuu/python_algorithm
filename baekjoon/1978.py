import sys

def is_prime_number(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x%i == 0:
            return False
    return True

# 참고 : https://freedeveloper.tistory.com/391

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

is_prime_number_count = 0

for i in numbers:
    if is_prime_number(i):
        is_prime_number_count += 1

print(str(is_prime_number_count))