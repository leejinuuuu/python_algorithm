from posixpath import split


s = input()

for i in range(1, 10):
    print(s + " * " + str(i) + " = " + str(int(s)*int(i)))
