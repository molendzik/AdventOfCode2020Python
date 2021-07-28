#read file and convert content to a useable list of strings
with open("input.txt", "r") as file:
    data = file.read().split("\n\n")
print(data)

answer_sum = 0
#check if \n is in the string, if so subtract 1 from set length
for answer in data:
    print(set(answer))
    if "\n" in set(answer):
        answer_sum += len(set(answer)) - 1
    elif "\n" not in set(answer):
        answer_sum += len(set(answer))
        print("no backslash")

print("Solution:", answer_sum)

