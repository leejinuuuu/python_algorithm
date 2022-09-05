# import sys
# import math
# import time


# N, K = map(int, sys.stdin.readline().split())

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# head = ListNode(1)
# cur_node = head

# start = time.time()
# for _ in range(2, N+1):
#     node = ListNode(_)
#     cur_node.next = node
#     cur_node=node
#     if _ == N:
#         cur_node.next = head
# # 원형 링크드 리스트(현재 위 for문에서 시간소요가 큼)


# end = time.time()
# print(f"{end - start:.10f} sec")
# start = time.time()

# node = head
# index = 0
# answer = []
# while node:
#     if index == K-1:
#         answer.append(str(node.val))

#         if node.next.val == node.val:
#             break

#         # 이전의 노드와 다음의 노드를 이어줌으로서 현재 노드를 제거
#         node = node.next
#         bef_node.next = node
#         index = 0
        
#     index+=1
#     bef_node = node
#     node=node.next

# # print("<",", ".join(answer),">", sep="")


# end = time.time()
# print(f"{end - start:.10f} sec")


import sys
from math import ceil, log2
input = sys.stdin.readline

def sol1168():
    n, k = map(int, input().split())
    cap = 2 ** ceil(log2(n))
    t = init_tree(n, cap)

    answer = []
    idx = k-1

    for _ in range(n-1):
        answer.append(query(t, cap, idx+1))
        n -= 1
        idx = (idx + k - 1) % n
    
    answer.append(query(t, cap, idx+1))

    return '<{}>'.format(', '.join(map(str, answer)))

def init_tree(n, cap):
    tree = [0] * (2*cap)
    tree[cap:cap+n] = [1]*n
    for i in range(cap-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]
    return tree
    
def query(tree, cap, idx):
    pos = 1
    while pos < cap:
        tree[pos] -= 1
        left, right = pos * 2, pos * 2 + 1
        if tree[left] >= idx:
            pos = left
        else:
            idx -= tree[left]
            pos = right
    tree[pos] -= 1
    return pos - cap + 1


if __name__ == "__main__":
    print(sol1168())

# 참고 : https://www.acmicpc.net/source/35128563