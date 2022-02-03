def TextTransform():
    print("Введите текст:")
    items = [str(el) for el in input().split()]
    Transform_str = ""
    for s in items:
        if s.islower() == True:
            Transform_str += s + " "
        else: Transform_str += s.upper() + " "
    print(Transform_str)

TextTransform()