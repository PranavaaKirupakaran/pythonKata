def square_digit(num):
    numString = str(num)
    numSquareString = ""
    for n in numString:
        numSquareString = numSquareString + str(int(n)*int(n))

    return int(numSquareString)

print(square_digit(9119))

