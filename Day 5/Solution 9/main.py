#read file and convert content to a list of lines
with open("input.txt", "r") as file:
    data = file.readlines()

for index, boarding_pass in enumerate(data):
    boarding_pass  = boarding_pass .rstrip("\n")
    data[index] = boarding_pass

highest_seat_id = 0 #base value of the highest seat

#separate row and column data
for boarding_pass in data:
    row = boarding_pass.rstrip("RL")
    column = boarding_pass.lstrip("FB")

    print(row, column)

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

    #calculate the seat id and find the highest one
    seat_id = row_number*8 + column_number
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id


print("Solution:", highest_seat_id)