S = list(input())

alphabet = [-1] * 26
for i in range(len(S)-1, -1, -1):
    alphabet[ord(S[i]) - 97] = i

for i in range(26):
    print(alphabet[i], end=" ")
