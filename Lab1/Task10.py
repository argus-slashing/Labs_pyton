def Shearch_Repeat(word):
    lenght = len(word)
    count = 0
    while word:
        for i in range (1, len(word)):
            if word[i] == word[0]:
                count += 1
        word = word.replace(word[0], '')
    return (count * 100) / lenght

def Shearch_Hard_Symbol(word, symbol):
    key = False
    while symbol:
        for i in range (0, len(word)):
            if word[i] == symbol[0]:
                key = True
                word = ""
                break
        symbol = symbol.replace(symbol[0], '')
    return key


password = input("Введите пароль: ")
hard_symbol = "!@#$%^&*()_+-=?/><"
complexyti = ""
if len(password) >= 12:
    complexyti += "*"
if (password.islower() == False) or (password.isdigit() == False):
    complexyti += "*"
Repeats = Shearch_Repeat(password)
if int(Repeats) <= 10:
    complexyti += "*"
if Shearch_Hard_Symbol(password, hard_symbol) == True:
    complexyti += "*"
print("Сложность пароля (макс. 4-звезд): ", complexyti)
print("* - Очень просто, ** - просто, *** - средне, **** - сложно")