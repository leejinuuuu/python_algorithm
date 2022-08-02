import sys

N = int(input())
for _ in range(N):
    is_vps = list(sys.stdin.readline())
    count_of_ps = 0
    for i in range(len(is_vps)):
        if is_vps[i] == "(":
            count_of_ps += 1
        elif is_vps[i] == ")":
            count_of_ps -= 1

        if count_of_ps < 0:
            break
    if count_of_ps == 0:
        print("YES")
    else:
        print("NO")
