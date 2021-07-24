#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()


#define function that will merge correct strings and remove empty ones
def merge_items(list):
    first_index = list.index(" ")
    list.remove(" ")

    if first_index < len(list) - 1 and " " in list:
        second_index = list.index(" ")

        while second_index > first_index + 1:
            list[first_index] = list[first_index] + list[first_index + 1]
            list.pop(first_index + 1)
            second_index -= 1

    elif first_index == len(list) - 1:
        list.pop(-1)

#remove \n from strings
for index, line in enumerate(data):
    line = line.replace("\n", " ")
    data[index] = line

#convert list to useable strings
data.append(" ") #marks the end of data for merge_items() and gets removed at the end
while " " in data:
    merge_items(data)

#byr, iyr, eyr, hgt, hcl, ecl, pid, cid
template1 = [1, 1, 1, 1, 1, 1, 1, 0]
template2 = [1, 1, 1, 1, 1, 1, 1, 1]
valid_counter = 0
#split each document (passport) and check for correct field types
for document in data:
    fields = document.split(" ")
    fields.pop(-1) #remove whitespace at the end of each document (which was used to separate them)
    print(fields)
    type_counter = [0, 0, 0, 0, 0, 0, 0, 0]

    for exact_field in fields:
        type = exact_field.split(":", 8)
        print(type)

        if "byr" in type:
            type_counter[0] = 1
        if "iyr" in type:
            type_counter[1] = 1
        if "eyr" in type:
            type_counter[2] = 1
        if "hgt" in type:
            type_counter[3] = 1
        if "hcl" in type:
            type_counter[4] = 1
        if "ecl" in type:
            type_counter[5] = 1
        if "pid" in type:
            type_counter[6] = 1
        if "cid" in type:
            type_counter[7] = 1
        print(type_counter)
    if type_counter == template1 or type_counter == template2:
        print("Found a valid passport.")
        valid_counter += 1

print("Solution:", valid_counter)