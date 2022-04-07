from posixpath import split

s = input()

h = int(s.split()[0])
m = int(s.split()[1])

if(m < 45):
    h = h-1
    m = (60+m)-45
else:
    m = m-45
    
if(h < 0):
    h = 23
print(str(h)+" "+str(m))
