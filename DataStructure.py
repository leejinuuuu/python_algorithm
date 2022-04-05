# 1. 리스트
# 시간복잡도 O(1)
from audioop import reverse
from operator import truediv
from threading import stack_size


array1 = []
array2 = [1, 2]
array3 = [[1, 2], 3]
array4 = [[1, 2], [3, 4]]

print(array3[0])
# -> [1,2]

# 2. 해시
# 시간복잡도 O(1)
dict1 = {1: "one", 2: "two", 3: "three"}

print(dict1.get(1))
# -> one

# 3. 스택


class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

# 스택을 활용해서 문자열을 뒤집는 함수


def reverseString(str):
    s = stack()
    result = ""

    for i in str:
        s.push(i)

    while s.isEmpty() != True:
        result += s.pop()

    return result


print(reverseString("abcdefg"))
# -> gfedcba

# 4. 큐


class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# 순차탐색
# 시간복잡도 O(n)
# for i in target.size

# 이분탐색
# 시간복잡도 O(log2 N) (오름차순으로 정렬되어있다는 전제하에)


class solve:
    def __init__(self, items):
        self.items = []
        self.items = items

    def where(self, i):
        m = 0
        s = 0
        e = len(self.items)

        while i != self.items[m]:
            m = int((s+e)/2)
            if i == self.items[m]:
                return m+1
            if i > self.items[m]:
                s = m+1
            else:
                e = m-1
        return -1


s = solve([1, 2, 3, 4, 5, 6, 7])
print(s.where(7))
# -> 7

# 그래프 순회 알고리즘
# 깊이 우선 탐색


def dfs(v):
    for i in G[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

# 너비 우선 탐색


def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        for i in G[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
