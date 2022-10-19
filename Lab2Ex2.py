
years = list()
firstPerson = str
secondPerson = str
FILENAME = "input2.txt"
with open(FILENAME, "r", encoding="utf8") as file:
    messages = file.read().splitlines()

    for i in range(0, len(messages), 1):
        str1 = str(messages[i]).split(';')
        str1 = str(str1[2]).split(' ')
        years.append(str1[0])
    maxYear = 0
    minYear = years[0]
    for i in range(0, len(years), 1):
        years[i] = int(years[i])
        if years[i] > maxYear or years[i] == 0:
            maxYear = years[i]
    for i in range(0, len(years), 1):
        if years[i] < int(minYear):
            minYear = years[i]
    for i in range(0, len(messages), 1):
        if str(maxYear) in messages[i].split(';')[2].split(' ')[0]:
            firstPerson = str(messages[i])
        if str(minYear) in messages[i].split(';')[2].split(' ')[0]:
            secondPerson = str(messages[i])
with open('output2.txt', 'w', encoding='utf8') as file:
    file.writelines(secondPerson + "\n")
    file.writelines(firstPerson)
