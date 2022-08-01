import sys

N = int(input())
m_stack = []
for _ in range(N):
    commands = []
    commands = list(map(str, sys.stdin.readline().split()))

    if commands[0] == "push":
        m_stack.append(commands[1])
    elif commands[0] == "pop":
        if len(m_stack) > 0:
            print(m_stack.pop())
        else:
            print("-1")
    elif commands[0] == "size":
        print(len(m_stack))
    elif commands[0] == "empty":
        if len(m_stack) == 0:
            print("1")
        else:
            print("0")
    elif commands[0] == "top":
        if len(m_stack) == 0:
            print("-1")
        else:
            print(m_stack[len(m_stack)-1])
