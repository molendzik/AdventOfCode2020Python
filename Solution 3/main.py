#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, line in enumerate(data):
    line = line.rstrip("\n")
    data[index] = line

#split strings into useable data, convert numbers to int, check if password is correct and (if it is) add it to the list
correct_passwords = []

for line in data:
    rules, password = line.split(": ")
    range, character = rules.split(" ", 1)
    minimum, maximum = range.split("-")
    minimum = int(minimum)
    maximum = int(maximum)
    if minimum <= password.count(character) <= maximum:
        correct_passwords.append(line)

print("Solution:", len(correct_passwords))
