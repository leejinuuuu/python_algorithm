import sys
sys.setrecursionlimit(10 ** 6)

A, P = map(int, sys.stdin.readline().split())

arr_list = []

while True:
    arr_list.append(str(A))

    sum = 0

    for i in range(len(str(A))):
        sum += int(str(A)[i]) ** P

    A = sum

    if str(A) in arr_list:
        print(str(arr_list.index(str(A))))
        break


