def InputArray(array, n):
    for i in range(n):
        s = "Введите " + str(i + 1) + " число: "
        array.append(int(input(s)))

def OutputArray(array):
    s = ""
    for i in array:
        s = s + str(i) + " "
    print(s)

# array: array_int, nel: int, compare: Callable[[int, int], int], swap: Callable[[int, int], None],
def bubblesort(array, nel):
    b = True

    def compare(num1, num2):
        if num1 < num2:
            return -1
        elif num1 == num2:
            return 0
        else:
            return 1

    def swap(array, id1, id2):
        buf = array[id1]
        array[id1] = array[id2]
        array[id2] = buf
        return array

    while b:
        b = False

        for i in range(nel - 1):
            if (compare(array[i], array[i + 1]) == 1):
                array = swap(array, i, i + 1)
                b = True

            if (compare(array[nel - 2 - i], array[nel - 1 - i]) == 1):
                array = swap(array, nel - 2 - i, nel - 1 - i)
                b = True
    return


if __name__ == '__main__':
    n = int(input("Введите кол-во чисел: "))

    array = []
    InputArray(array, n)
    OutputArray(array)

    bubblesort(array, n)
    OutputArray(array)
