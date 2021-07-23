#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, line in enumerate(data):
    line = line.rstrip("\n")
    data[index] = line

#1 line has 31 characters with indexes 0-30; data has 323 lines with indexes 0-322

x_coordinate = 0
y_coordinate = 0
predicted_path = []

while True:
    predicted_path.append(data[y_coordinate][x_coordinate])

    y_coordinate += 1
    if y_coordinate == 323:
        break
    x_coordinate += 3
    if x_coordinate >= 31:
        x_coordinate -= 31

print("Solution:", predicted_path.count("#"))