while True:
    try:
        S = list(input())

        lower, upper, number, blank = 0, 0, 0, 0

        for i in range(len(S)):
            s = ord(S[i])
            if(s >= 97 and s <= 122):
                lower += 1
            elif(s >= 65 and s <= 90):
                upper += 1
            elif(s == 32):
                blank += 1
            else:
                number += 1

        print(str(lower) + " " + str(upper) +
              " " + str(number) + " " + str(blank))
    except EOFError:
        break
