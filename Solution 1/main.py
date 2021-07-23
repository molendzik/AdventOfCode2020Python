#read file and convert content to a list of ints
with open("input.txt", "r") as file:
    data = file.readlines()

for index, number in enumerate(data):
    number.rstrip("\n")
    number = int(number)
    data[index] = number

#sort the list and find the solution
data.sort()
while(True):
    if (data[-1] + data[0] > 2020):
        data.pop(-1)
    elif (data[-1] + data[0] < 2020):
        data.pop(0)
    else:
        print("Numbers:", data[-1], data[0], "Sum:", data[-1] + data[0], "Result:",  data[-1] * data[0])
        break

