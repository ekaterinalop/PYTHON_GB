# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from ast import iter_child_nodes


original = []
data1 = open('hw5_1.txt', 'r')
for line in data1:
    original.append(line)    #ВОПРОС К ПРЕПОДАВАТЕЛЮ: Как убрать '\n' в записи элемента списка (в файле несколько строк)?
data1.close()

result = ''
for item in original:
    i = 0
    while i < len(item):
        count = 1
        while i+1 < len(item) and item[i] == item[i+1]:
            count += 1
            i = i+1
        result += str(count)+item[i]
        i = i+1

print(result)

data2 = open('hw5_2.txt', 'w')
data2.writelines(result)
data2.close()
