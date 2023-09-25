c = 4 % 1

a = bin(int(input("Введите число a: ")))[2:]

b = int(input("Введите число b: "))

m = int(input("Введите число m: "))

res = 0

for i in range(len(a)):
    res += (int(a[i]) * 2**(len(a) - 1 - i) * b)

print(res % m)


