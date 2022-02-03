def Bankomat():
    bills = [5000, 2000, 1000, 500, 200, 100, 50]
    cash = []
    for i in range (len(bills)):
        print()
        cash.append(input(f"Введите к-во {bills[i]}-рублёвых купюр: "))
    extradite = input("Введите необходимую сумму: ")
    sum = 0
    for i in range(len(bills)):
        sum += int(bills[i]) * int(cash[i])
    if int(extradite) > sum:
        print("Операция не может быть выполнена!")
    else:
        result = ""
        money = 0
        count = 0
        for i in range(len(bills)):
            while money < int(extradite) and count <= int(cash[i]):
                money += bills[i]
                count += 1
            money -= bills[i]
            count -= 1
            result += str(bills[i]) + "*" + str(count) + " "
            if money == extradite:
                break
        print(result)

Bankomat()