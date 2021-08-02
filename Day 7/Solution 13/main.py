with open("input.txt", "r") as file:
    data = file.readlines()

correct_colors = []

def find_colors(base_color):
    for line in data:
        color = line.split(" bags contain ")
        color[1] = color[1].rstrip("\n")

        if base_color in color[1] and color[0] not in correct_colors:
            correct_colors.append(color[0])
            find_colors(color[0])


find_colors("shiny gold")
print(correct_colors)
print("Solution:", len(correct_colors))
