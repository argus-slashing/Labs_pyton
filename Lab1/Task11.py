def Range(start, stop, move):
    i = start
    while i < stop:
        print ("i:", i)
        i += move

str = [int(el) for el in input("range ").split()]
if len(str) == 3:
    Range(str[0], str[1], str[2])
elif len(str) == 2:
    Range(str[0], str[1], 1)
else: Range(0, str[0], 1)