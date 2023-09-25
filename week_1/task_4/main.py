A = str(1 * 10**32)
B = str(1 * 10**32)

for i in range(32):
    num = int(input("Введите число, принадлежащее множеству A, если таких чисел больше не осталось, введите 100: "))
    if (num == 100):
        break
    A = str(int(A) + 10**num)

for i in range(32):
    num = int(input("Введите число, принадлежащее множеству B, если таких чисел больше не осталось, введите 100: "))
    if (num == 100):
        break
    B = str(int(B) + 10**num)

print(A)
print(B)

for i in range(32):
    if (A[32 - i] == B[32 - i] == '1'):
        print(i)