def FactorialZeros(n):
    col_5 = 0

    for i in range(n - n % 5, 0, -5):
        if (i == 0):
            break

        for b in range(2**10):
            if (i % 5 == 0):
                col_5 += 1
                i = i / 5
            else:
                break

    return col_5

print(FactorialZeros(100))

