# n = input()
# for i in range(1, len(n)+1):
#     print(n[i-1], end="")
#     if i % 10 == 0 and i != 0:
#         print()

A = input()
# i를 0부터 A의 길이만큼 반복하는데, 구간은 10개씩 증가
for i in range(0, len(A), 10):
    # 0부터 10, 11부터 20 이런 식으로 출력해야하기 떄문에, i:i+10을 할 경우, 10개씩 출력한다.
    print(A[i:i+10])
