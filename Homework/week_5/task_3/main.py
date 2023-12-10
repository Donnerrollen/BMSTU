from itertools import combinations
def InputArray(array, n):
    for i in range(n):
        s = "Введите " + str(i + 1) + " число: "
        array.append(int(input(s)))

def OutputArray(array):
    s = ""
    for i in array:
        s = s + str(i) + " "
    print(s)

def SumArrN(sum, n):
    k = n
    while sum >= k:
        if sum == k:
            return 1
        if sum > k:
            k = k * n
    return 0

if __name__ == '__main__':
    n = int(input("Введите кол-во чисел: "))

    res = []

    array = []
    InputArray(array, n)
    OutputArray(array)

    for i in range(1, n + 1):
        b = list(combinations(array, i))

        for elem in b:
            if (SumArrN(sum(elem), n)) == 1:
                res.append(elem)

print(res)