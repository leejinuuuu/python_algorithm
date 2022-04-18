import sys

N = int(input())

count = 0

for n in range(1, N+1):
    if n < 100:
        count += 1
    else:
        dif = int(str(n)[0]) - int(str(n)[1])
        for s in range(1, len(str(n))):
            if dif != int(str(n)[s-1])-int(str(n)[s]):
                break
            if s == len(str(n))-1:
                count += 1

print(count)
