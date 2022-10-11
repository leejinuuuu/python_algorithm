import math

string_array = []

while True:
    n = int(input())
    if n == 0:
        break

    if(n>=6):
        array = [ True for i in range(n+1)]

        for i in range(2, int(math.sqrt(n)) + 1):
            if array[i] == True:
                j=2
                while i*j<=n:
                    array[i*j]=False
                    j+=1

# 참고 : https://coding-of-today.tistory.com/170?category=995820
        result_list = []
        for i in range(2, n+1):
            if(array[i] and i%2 == 1):
                result_list.append(i)
        
        a, b = 1000000, 3
        breaker = False
        for i in range(len(result_list)):
            a=result_list[i]
            for j in range(len(result_list)-1, i-1, -1):
                if result_list[j]>b and a+result_list[j]==n:
                    b=result_list[j]
                    breaker = True
                    break
            if breaker:
                break
        if breaker == False:
            print("Goldbach's conjecture is wrong.")


        string_array.append(str(n)+" = "+str(a)+" + "+str(b))

for _ in range(len(string_array)):
    print(string_array[_])