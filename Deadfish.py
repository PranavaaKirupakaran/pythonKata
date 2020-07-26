def parse(data):
    value = 0
    arrayValue = []
    for n in data:
        if n == "i":
            value += 1
        elif n == "d":
            value -= 1
        elif n == "s":
            value = value*value
        elif n == "o":
            arrayValue.append(value)
    
    return arrayValue

print(parse("ooo"))
print(parse("ioioio"))
print(parse("idoiido"))
print(parse("codewars"))
