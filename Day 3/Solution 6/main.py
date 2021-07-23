#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, line in enumerate(data):
    line = line.rstrip("\n")
    data[index] = line

#1 line has 31 characters with indexes 0-30; data has 323 lines with indexes 0-322


def tree_counter(right_movement, down_movement):
    x_coordinate = 0
    y_coordinate = 0
    predicted_path = []

    while True:
        predicted_path.append(data[y_coordinate][x_coordinate])

        y_coordinate += down_movement
        if y_coordinate > 322:
            break
        x_coordinate += right_movement
        if x_coordinate >= 31:
            x_coordinate -= 31

    return predicted_path.count("#")

print("Slope 1:", tree_counter(1,1))
print("Slope 2:", tree_counter(3,1))
print("Slope 3:", tree_counter(5,1))
print("Slope 4:", tree_counter(7,1))
print("Slope 5:", tree_counter(1,2))
print("Solution:", tree_counter(1,1)*tree_counter(3,1)*tree_counter(5,1)*tree_counter(7,1)*tree_counter(1,2))