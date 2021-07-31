#read file and convert content to a useable list of strings
with open("input.txt", "r") as file:
    data = file.read().split("\n\n")
#print(data)

answer_sum = 0

#find duplicate answers in each group and add them to answer_sum
for answer in data:
    answers_separated = answer.split("\n")
    #print(answers_separated)
    for person in answers_separated:
        person = set(person)
    temp = set(answers_separated[0]).intersection(*set(answers_separated))
    answer_sum += len(temp)
    #print(len(temp))

print("Solution:", answer_sum)

