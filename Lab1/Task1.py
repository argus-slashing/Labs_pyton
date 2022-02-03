def get_count(str):
    tmp = 0
    for i in str:
        tmp +=1
        if i == ".":
            break
    return(len(str) - tmp)

def transform():
    s = input("Введите число:")
    cash = s.replace(",",".")
    count = get_count(cash)
    if float(cash) < 0.00:
        print("Некорректный формат!")
    else:
        key = float(cash)%1
        print(int(float(cash) - key),"рублей", int(key*10**count), "копеек")

transform()
