FILENAME1 = "input4.1.txt"
FILENAME2 = "input4.2.txt"
FILENAME3 = "output4.txt"
with open(FILENAME1, "r", encoding="utf8") as file:
    list1 = file.readlines()
with open(FILENAME2, "r", encoding="utf8") as file:
    list2 = file.readlines()

duplicates = set(list1) & set(list2)

# list1 = list(set(list1))
# list2 = list(set(list2))
# general = list1 + list2
# for item in general:
#     count = 0
#     for x in general:
#         if x == item:
#             count += 1
#     occurrences.append(count)
# duplicates = set()
# index = 0
# while index < len(general):
#     if occurrences[index] != 1:
#         duplicates.add(general[index])
#     index += 1
with open(FILENAME3, 'w', encoding="utf8") as file:
    file.writelines(duplicates)


