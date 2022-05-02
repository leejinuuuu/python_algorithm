# arr = []
# while True:
#     line = input()

#     if line == "":
#         break
#     else:
#         arr.append(line)

# for i in range(len(arr)):
#     print(arr[i])

while True:
    try:
        print(input())
    except EOFError:
        break
