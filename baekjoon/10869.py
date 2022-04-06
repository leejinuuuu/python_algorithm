from posixpath import split


s = input()
print(int(s.split()[0])+int(s.split()[1]))
print(int(s.split()[0])-int(s.split()[1]))
print(int(s.split()[0])*int(s.split()[1]))
print(int(int(s.split()[0])/int(s.split()[1])))
print(int(s.split()[0]) % int(s.split()[1]))
