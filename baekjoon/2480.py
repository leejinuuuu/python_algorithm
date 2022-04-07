from posixpath import split

s = input()

first = int(s.split()[0])
second = int(s.split()[1])
third = int(s.split()[2])

if(first == second and first == third):
    result = 10000+(first*1000)
elif((first == second and first != third) or (first == third and first != second)):
    result = 1000+first*100
elif((second == third and second != first)):
    result = 1000+second*100
else:
    if(first >= second and first >= third):
        result = first*100
    elif(second >= first and second >= third):
        result = second*100
    else:
        result = third*100

print(result)
