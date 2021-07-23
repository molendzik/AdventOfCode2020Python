#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, line in enumerate(data):
    line = line.rstrip("\n")
    data[index] = line

#split strings into useable data, convert numbers to int, check if password is correct and (if it is) add it to the list
correct_passwords = []

for line in data:
    matching_letters = 0

    rules, password = line.split(": ")
    range, character = rules.split(" ", 1)
    first_occurrence, second_occurrence = range.split("-")
    first_occurrence = int(first_occurrence)
    second_occurrence = int(second_occurrence)

    if password[first_occurrence-1] == character:
        matching_letters += 1
    if password[second_occurrence-1] == character:
        matching_letters += 1

    if matching_letters == 1:
        correct_passwords.append(line)

print("Solution:", len(correct_passwords))
