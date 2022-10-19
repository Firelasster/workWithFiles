# Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем записать их произведение в файл output.txt
import os.path

try:
    product = 1
    with open("input1.txt", "r") as file:
        number = file.readlines()[0].split(' ')
    with open('output.txt', 'w') as out:
        for i in range(int(number[0]), len(number), 1):
            product = product * int(number[i])
        out.write(str(int(product)))
    print('Запись завершена...')
except IOError as e:
    print(u'не удалось открыть файл')
    print(e)
