import sys

s = int(sys.stdin.readline())

for i in range(1, s+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
