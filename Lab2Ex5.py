import re
from collections import Counter

general = list()
latin = list()
symbols = list()
with open("input5.txt", "r", encoding="utf8") as file:
    text = file.readlines()
for i in range(0, len(text), 1):
    general.append(text[i])
general = [s.rstrip() for s in general]
for i in range(0, len(general), 1):
    for c in general[i]:
        symbols.append(c)
for i in range(0, len(symbols), 1):
    if re.search(r'[a-zA-Z]', symbols[i]):
        latin.append(symbols[i].lower())
result = dict(Counter(latin))
sorted_dict={}
sorted_keys=sorted(result, key=result.get, reverse=True)
for w in sorted_keys:
    sorted_dict[w]=result[w]
with open("output5.txt", "w", encoding='utf8') as file:
    file.writelines(str(sorted_dict))