import random

case = input("1 - Массив случайных чисел\n2-Массив с клавиатуры\n")
if case == "1":
    items = [random.randint(0, 100) for i in range(15)]
else:
    print("Введите значения через пробел")
    items = [int(el) for el in input().split()]
flug = True
for i in range (len(items) - 1):
    if items[i] > items[i + 1]:
        flug = False
        break
print(flug)