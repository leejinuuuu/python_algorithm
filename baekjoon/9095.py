T = int(input())
s = [1, 2, 4]
for i in range(3, 11):
    s.append(s[i-3]+s[i-2]+s[i-1])
ar = []
for i in range(T):
    ar.append(int(input()))
for i in range(0, T):
    print(s[ar[i]-1])
