N = int(input("Введите количество участников события: "))

K = int(input("Введите число K: "))

A = []
for x in range(N):
    A.append(x)

sum = -1

m = len(A)

while (len(A) != 1):
    print(A)
    sum += K
    sum = sum % len(A)
    A.pop(sum)
    sum -= 1

print(A)