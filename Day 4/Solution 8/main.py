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
#define function checking for hexadecimal numbers
def is_hex(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False

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
    #print(fields)
    type_counter = [0, 0, 0, 0, 0, 0, 0, 0]

    for exact_field in fields:
        type = exact_field.split(":", 8)
        #print(type)

        if "byr" == type[0]:
            if int(type[1]) >= 1920 and int(type[1]) <=2002:
                type_counter[0] = 1

        elif "iyr" == type[0]:
            if int(type[1]) >= 2010 and int(type[1]) <=2020:
                type_counter[1] = 1

        elif "eyr" == type[0]:
            if int(type[1]) >= 2020 and int(type[1]) <= 2030:
                type_counter[2] = 1

        elif "hgt" == type[0]:
            if type[1][-2] == "c" and type[1][-1] == "m":
                type[1] = type[1].rstrip("cm")
                if int(type[1]) >= 150 and int(type[1]) <= 193:
                    type_counter[3] = 1
            elif type[1][-2] == "i" and type[1][-1] == "n":
                type[1] = type[1].rstrip("in")
                if int(type[1]) >= 59 and int(type[1]) <= 76:
                    type_counter[3] = 1

        elif "hcl" == type[0]:
            if type[1][0] == "#":
                type[1] = type[1].lstrip("#")
                if is_hex(type[1]) == True:
                    type_counter[4] = 1

        elif "ecl" == type[0]:
            if type[1] == "amb" or type[1] == "blu" or  type[1] == "brn" or type[1] == "gry" or type[1] == "grn" or type[1] == "hzl" or type[1] == "oth":
                type_counter[5] = 1

        elif "pid" == type[0]:
            if type[1].isnumeric() and len(type[1]) == 9:
                type_counter[6] = 1

        elif "cid" == type[0]: #meaningless
            type_counter[7] = 1
        #print(type_counter)

    if type_counter == template1 or type_counter == template2:
        #print("Found a valid passport.")
        valid_counter += 1

print("Solution:", valid_counter)