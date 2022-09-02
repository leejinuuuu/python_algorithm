import sys

N, K = map(int, sys.stdin.readline().split())

circle = [_ for _ in range(1, N+1)]
answer = []
index = 0

for _ in range(N):
    index += K-1
    if index >= len(circle):
        index = index%len(circle)
    answer.append(str(circle.pop(index)))

print("<", ", ".join(answer),">", sep="")

# 참고 : https://infinitt.tistory.com/213

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head = ListNode(1)
# cur_node = head

# for _ in range(2, N+1):
#     new_node = ListNode(_)
#     cur_node.next = new_node
#     cur_node = cur_node.next
    
#     if _ == N:
#         new_node.next = head

# node = head
# dif = K
# while node:
#     if dif > 1:
#         node=node.next
#         dif-=1
#     else:
#         print(node.val)
#         if node.next.next != None:
#             node.next = node.next.next
#         dif=K

# 원형 연결 리스트로 풀려고 했으나 실패