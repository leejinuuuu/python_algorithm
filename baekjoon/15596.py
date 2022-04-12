def solve(a: list) -> int:
    #  "->" : return 값 관련된 주석
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum
