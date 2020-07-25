def find_short(s):
    stringSplit = s.split(" ")
    shortWord = 0
    for n in stringSplit:
        if shortWord == 0:
            shortWord = len(n)
        elif shortWord > len(n):
            shortWord = len(n)

    return shortWord

print(find_short("Dat boi from down da street"))
