def ShearchChar():
    str = input("Введите текст: ")
    word = str.lower()
    while word:
        key = True
        for i in range (1, len(word)):
            if word[i] == word[0]:
                key = False
                break
        if key: 
            print(word[0])
        word = word.replace(word[0], '')

ShearchChar()