N = int(input())

s = [1, 1, 2]

for i in range(3, 91):
    s.append(s[i-1] + s[i-2])

print(s[N-1])
