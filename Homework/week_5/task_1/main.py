def BinarySearch(array, element, TypeOfSorting, left, right):
    while(True):
        middle = (left + right) // 2
        if left > right:
            return -1
        elif element == array[middle]:
            return middle
        elif TypeOfSorting * element > TypeOfSorting * array[middle]:
            left = middle + 1
        elif TypeOfSorting * element < TypeOfSorting * array[middle]:
            right = middle - 1

def Output(array):
    s = ""
    for i in array:
        s = s + str(i)+ " "
    print(s)

if __name__ == '__main__':
    arr = [-15, -10, -5, 25, 78, 100, 102, 180]
    arr.reverse()

    """
    n = int(input("Введите размер массива: "))


    for i in range(n):
        print("Введите ", i + 1, "элемент массива")
        arr.append(int(input()))

    print("Введите элемент, который нужно найти")
    el = int(input())
    """

    Output(arr)
    index = BinarySearch(arr,  -5, -1, 0, len(arr) - 1)
    print(index)