A = []

n = int(input("Введите число n: "))

x = int(input("Введите x: "))

for a in range(n + 1):
    s = "Введите a_" + str(n - a) + ": "
    A.append(int(input(s)))

res_1 = A[0]
res_2 = A[0]
print(A)

for id_a in range(n):
    res_1 = res_1 * x + A[id_a + 1]
    if (id_a != n - 1):
        res_2 = (n - id_a) * res_2 + A[id_a + 1]

print("f(x) = ", res_1)
print("f'(x) = ", res_2)