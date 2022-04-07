from posixpath import split

s = input()

h = int(s.split()[0])
m = int(s.split()[1])

t = int(input())

h += int((m+t)/60)
m = m+t

if(m > 59):
    m -= int(m/60)*60

if(h >= 24):
    h -= 24

print(str(h)+" "+str(m))
