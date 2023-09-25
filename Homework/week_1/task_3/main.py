Fib_nums = [1, 1]
Arr_sum_nums = []

x = int(input("Введите число x: "))

for i in range(2, 2**10):
    if (Fib_nums[i - 2] + Fib_nums[i - 1] <= x):
        Fib_nums.append(Fib_nums[i - 2] + Fib_nums[i - 1])
    else:
        break

Fib_nums.reverse()

for i in range(len(Fib_nums)):
    if (x - Fib_nums[i] > 0):
        x = x - Fib_nums[i]
        Arr_sum_nums.append(Fib_nums[i])
    if (x - Fib_nums[i] == 0):
        Arr_sum_nums.append(Fib_nums[i])
        break

print(Arr_sum_nums)
