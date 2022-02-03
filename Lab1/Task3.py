def SaverCards():
    key = True
    while key:
        num = input("Введите номер карты:")
        if len(num) > 16:
            print("Ошибка!Попробуйте еще раз!")
        else: key = False
    print(num[0:4] + "********" + num[12:16])
    
    


SaverCards()