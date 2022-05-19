N = int(input())
s = [0, 1, 3, 5]
for i in range(4, 1001):
    s.append(s[i-2]*2+s[i-1])

print(s[N] % 10007)

# 참고 : https://pacific-ocean.tistory.com/194
