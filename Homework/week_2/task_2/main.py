x = int(input("Введите число x: "))

arr = []

for i in range(x + 1):
    arr.append(i)

for dl in range(2, x + 1):
    for i in range(len(arr)):
        if (arr[i] % dl == 0) and (arr[i] != dl):
            arr[i] = 0
    if 0 in arr:
        arr.remove(0)

mxd = 0
for dl in arr:
    if x % dl == 0:
        mxd = dl

print(mxd)