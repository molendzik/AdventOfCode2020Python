#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, boarding_pass in enumerate(data):
    boarding_pass  = boarding_pass .rstrip("\n")
    data[index] = boarding_pass

row_list = []
column_list = []
seat_list = []

#separate row and column data
for boarding_pass in data:
    row = boarding_pass.rstrip("RL")
    column = boarding_pass.lstrip("FB")

    #print(row, column)

    # find the value
    row_temp = [0, 127]
    column_temp = [0,7]

    for letter in row:
        if letter == "F":
            row_temp[1] -= ((row_temp[1] - row_temp[0] + 1) / 2)
            #print(row_temp)
        elif letter == "B":
            row_temp[0] += ((row_temp[1] - row_temp[0] + 1) / 2)
            #print(row_temp)
    for letter in column:
        if letter == "L":
            column_temp[1] -= ((column_temp[1] - column_temp[0] + 1) / 2)
            #print(column_temp)
        elif letter == "R":
            column_temp[0] += ((column_temp[1] - column_temp[0] + 1) / 2)
            #print(column_temp)

    #check if value is correct and convert to int
    if row_temp[0] == row_temp[1]:
        row_number = int(row_temp[0])
        #print(row_number)
    if column_temp[0] == column_temp[1]:
        column_number = int(column_temp[0])
        #print(column_number)
    seat_list.append([row_number, column_number])

#sort the list and find the missing seat
seat_list.sort()
for index, seat in enumerate(seat_list):
    if 0 < index < len(seat_list)-1:

        if seat[1] + 1 != seat_list[index+1][1] and seat[0] + 1 != seat_list[index+1][0]:
            print(seat)
            if seat[1] != 7:
                correct_row_column = [int(seat[0]), int(seat[1])+1]
            else:
                correct_row_column = [int(seat[0]) + 1, 0]



solution = correct_row_column[0]*8 + correct_row_column[1]
print("Solution:", solution)




