S = list(input())

alphabet = [0] * 26

for i in range(len(S)):
    alphabet[ord(S[i]) - 97] = alphabet[ord(S[i]) - 97] + 1

for i in range(len(alphabet)):
    print(alphabet[i], end=" ")
