from array import array
import random
import math 

def N_Generator():
    n = random.randint(1, 100)
    items = [random.randint(0, 100) for i in range(n)]
    count = 0
    point = 0
    while point < n:
        point = 2 ** count
        count += 1
    right = point - n
    left = n - point ** (count - 1)
    if left > right:
        size = left
    else:
        size = right
    array = []
    for i in range (len(items) - 1):
        array.append(items[i])
    for i in range(n, n + int(size) - 1):
        array.append(0)
    
    print(f"Массив увеличился на {int(size)} элементов")
N_Generator()