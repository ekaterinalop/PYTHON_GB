message = '''Что делаем?
0-поиск и просмотр
1-добавить запись
2-удалить запись под номером N
3-записать в файл
4-выход\n'''


def display_data(data):
    for line in data:
        print(line)


def display_menu():
    answer = int(input(message))
    return answer

def search(data):
    item=str(input("Введите класс для поиска данных по студентам или пробел для просмотра всех: "))
    if item==' ':
        display_data(data)
    else: 
        for i in range(len(data)):
            if data[i][2] == item:
                print (data[i])
    



