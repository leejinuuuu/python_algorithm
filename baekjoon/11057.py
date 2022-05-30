N = int(input())
s = [[1]*10 for i in range(1000)]
for i in range(1, 1000):
    for j in range(1, 10):
        s[i][j] = s[i][j-1] + s[i-1][j]
print(s[N-1])
print(sum(s[N-1]) % 10007)
