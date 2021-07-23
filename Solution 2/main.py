#read file and convert content to a list of ints
with open("input.txt", "r") as file:
    data = file.readlines()

for index, number in enumerate(data):
    number.rstrip("\n")
    number = int(number)
    data[index] = number

#find the solution
for number1 in data:
    for number2 in data:
        if 2020-(number1 + number2) in data:
            print("Numbers:", number1, number2, 2020-(number1 + number2), "Solution:", (2020-(number1 + number2)) * number1 * number2)

