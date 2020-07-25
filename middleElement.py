input1 = input("Element 1: \n")
input2 = input("Element 2: \n")
input3 = input("Element 3: \n")

input_array = [input1, input2, input3]
inputCopy = [input1, input2, input3]
inputCopy.sort()
print(input_array)
print(input_array.index(inputCopy[1]))
