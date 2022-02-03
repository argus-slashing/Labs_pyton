def SeparatorTxt():
    print("Введите текст:")
    items = [str(el) for el in input().split()]
    _very_big = ""
    _big = ""
    _small = ""
    for i in items:
        if len(i) > 7:
            _very_big += i + " "
        if len(i) >= 4 and len(i) <= 7:
            _big += i + " "    
        if len(i) < 4:
            _small += i + " "
    print(_very_big, "\n", _big, "\n", _small)



SeparatorTxt()        