#Вывод массива
def OutputArray(array):
    s = ""
    for i in array:
        s = s + i + " "
    print(s)

#Ввод массива
def InputArray(array):
    for i in range(n):
        s = "Введите " + str(i+1) + " строчку: "
        array.append(str(input(s)))

#Функция находит максимальное кол-во символов в стыке строк слева
def LeftJoint(string1, string2):
    countJoint = 0
    for i in range( min(len(string1), len(string2)) ):
        if string2[-i:] == string1[:i]:
            countJoint = i
    return countJoint

#Функция находит максимальное кол-во символов в стыке строк справа
def RightJoint(string1, string2):
    countJoint = 0
    for i in range( min(len(string1), len(string2)) ):
        if string2[:i] == string1[-i:]:
            countJoint = i
    return countJoint

#Нахождение наилучшего стыка для данной пары строк(с максимальным кол-ом символов) : правый, левый, обоюдосторонний
def CountWordsInBestJoint(string1, string2):
    if (RightJoint(string1, string2) > LeftJoint(string1, string2)):
        return ["right", RightJoint(string1, string2)]
    elif (RightJoint(string1, string2) < LeftJoint(string1, string2)) :
        return ["left", LeftJoint(string1, string2)]
    else: return ["both", LeftJoint(string1, string2)]

#Находит стыки всех пар строк
def FindAllBestJoint(array_strings):
    ArrAllJoint = []
    for i in range(len(array_strings) - 1):
        for j in range(i + 1, len(array_strings)):
            ArrAllJoint.append([CountWordsInBestJoint(array_strings[i], array_strings[j]), i, j])
    return ArrAllJoint

#Хехе, находит наилучший стык из всех пар строк
def FindMaxBestJooint(array_joints):
    ArrayMaxJoints = ["", -1, -1, -1]

    for i in array_joints:
        if i[0][1] > ArrayMaxJoints[1]:
            ArrayMaxJoints[0] = i[0][0]
            ArrayMaxJoints[1] = i[0][1]
            ArrayMaxJoints[2] = i[1]
            ArrayMaxJoints[3] = i[2]

    return ArrayMaxJoints

#Функция слияния строк с наилучшим стыком
def MergeStrings(ArrayJoints, ArrayStrings):
        if ArrayJoints[0] == "right":
            s = ArrayStrings[ArrayJoints[2]] + ArrayStrings[ArrayJoints[3]][ArrayJoints[1]:]
            ArrayStrings.append(s)
            ArrayStrings.pop(ArrayJoints[2])
            ArrayStrings.pop(ArrayJoints[3] - 1)
        if ArrayJoints[0] == "left":
            s = ArrayStrings[ArrayJoints[3]] + ArrayStrings[ArrayJoints[2]][ArrayJoints[1]:]
            ArrayStrings.append(s)
            ArrayStrings.pop(ArrayJoints[2])
            ArrayStrings.pop(ArrayJoints[3] - 1)
        if ArrayJoints[0] == "both":
            s = ArrayStrings[ArrayJoints[3]] + ArrayStrings[ArrayJoints[2]][ArrayJoints[1]:]
            ArrayStrings.append(s)
            ArrayStrings.pop(ArrayJoints[2])
            ArrayStrings.pop(ArrayJoints[3] - 1)

#Функция слияния в одну строку
def FindLengthShortesetString(array):
    while(len(array) > 1):
        a = FindAllBestJoint(array)
        b = FindMaxBestJooint(a)
        MergeStrings(b, array)

    return array[0]

if __name__ == '__main__':
    n = int(input("Введите кол-во строк: ")) #Кол-во строк

    array_of_strings = []

    InputArray(array_of_strings)
    OutputArray(array_of_strings)

    '''
    print(FindAllBestJoint(array_of_strings))
    print(FindMaxBestJooint(FindAllBestJoint(array_of_strings)))

    MergeStrings(FindMaxBestJooint(FindAllBestJoint(array_of_strings)), array_of_strings)

    OutputArray(array_of_strings)
    '''

    print(FindLengthShortesetString(array_of_strings))
    print(len(FindLengthShortesetString(array_of_strings)))