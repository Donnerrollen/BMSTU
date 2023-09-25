arr = []

print("Введите массив. Если элементов больше не осталось, ввелите - ")

for i in range(10000):
    num = input()
    if (num == "-"):
        break
    else:
        arr.append(int(num))

#print(arr)

k = int(input("Введите k: "))

sum = 0

for i in range(k):
    sum += arr[i]

#print(sum)
mx = 0

for i in range(k, len(arr)):
    sum += arr[i] - arr[i - k]
    mx = max(mx, sum)

print(mx)