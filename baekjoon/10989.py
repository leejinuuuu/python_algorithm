import sys

N = int(input())
numbers = [0] * 10001
for _ in range(N):
    input_num = int(sys.stdin.readline())

    numbers[input_num-1] = numbers[input_num-1]+1

for i in range(10000):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i+1)

# 참고 : https://somjang.tistory.com/entry/Mxmxmxm
