import sys

S = sys.stdin.readline()

return_list = []
for _ in range(0, len(S)-1):
    return_list.append(S[_:len(S)-1])

return_list.sort()

for _ in range(len(return_list)):
    print(return_list[_])