from posixpath import split


s = input()
A = int(s.split()[0])
B = int(s.split()[1])
C = int(s.split()[2])

print(((A+B) % C))
print(((A % C)+(B % C)) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)
