n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))

arr = [ [0]*n for i in range(m)]
arr_min_stol = [[float("inf")]*3 for i in range(n)]
arr_max_strok = [[float("-inf")]*3 for i in range(m)]

for y in range(n):
    for x in range(m):
        s = "Введите значение элемента a" + str(y + 1) + str(x + 1) + ": "
        arr[y][x] = int(input(s))

print(arr)

for y in range(n):
    for x in range(m):
        elem = arr[y][x]

        if elem > arr_max_strok[y][0]:
            arr_max_strok[y][0] = arr[y][x]
            arr_max_strok[y][1] = x
            arr_max_strok[y][2] = y
        if elem < arr_min_stol[x][0]:
            arr_min_stol[x][0] = arr[y][x]
            arr_min_stol[x][1] = x
            arr_min_stol[x][2] = y

print(arr_max_strok)
print(arr_min_stol)

sedl_elem = []

for a in arr_max_strok:
    for b in arr_min_stol:
        if a[0] == b[0]:
            sedl_elem.append(a[0])
if len(sedl_elem) != 0:
    print(sedl_elem)
else:
    print("None")