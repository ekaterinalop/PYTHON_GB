# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# !!!<<<<< Не сделано.>>>>>>

data1 = open('hw5_1.txt', 'r')
for line1 in data1:
    print(line1)
data1.close()

copy1 = line1[:-2].split('x')

mult_list = list(filter(lambda x: x != '*', copy1))

print(copy1, mult_list)


data2 = open('hw5_2.txt', 'r')
for line2 in data2:
    print(line2)
data2.close()

result
data = open('hw5_res.txt', 'w')
data.writelines(result)
data.close()
print(data)
