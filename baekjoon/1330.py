from posixpath import split


s = input()

a = int(s.split()[0])
b = int(s.split()[1])

if(a > b):
    print(">")
elif(a < b):
    print("<")
else:
    print("==")
