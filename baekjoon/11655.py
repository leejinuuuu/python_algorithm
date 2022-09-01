N = list(input())

for i in range(len(N)):
    # if((N[i] >= 97 and N[i] <= 122) or (N[i] >= 65 and N[i] <=90))
    if(N[i].isalpha()):
        if(N[i].isupper()):
            N[i]=ord(N[i])+13-26 if ord(N[i])+13>90 else ord(N[i])+13
        else:
            N[i]=ord(N[i])+13-26 if ord(N[i])+13>122 else ord(N[i])+13
    else:
        N[i]=ord(N[i])
        
# 리스트 배열이 문자로 이뤄지지 않았을 경우, 리스트 문자열로 변환한 뒤 문자열로 바꾼다.
print("".join(str(chr(_)) for _ in N))