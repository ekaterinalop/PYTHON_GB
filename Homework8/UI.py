import display 
import fileio

def menu(data):
    while True:
        answer = display.display_menu()
        if answer == 0:
            display.search(data)
        elif answer == 1:
            str_data = input("Введите данные с разделителем ; ")
            row = str_data.split(";")
            data.append([row[0], row[1], row[2], row[3]])
        elif answer == 2:
            str_to_del = input("Введите ID: ")
            for i in range(len(data)):
                if data[i][0] == str_to_del:
                    del (data[i])
        elif answer == 3:
            fileio.write_data("data.csv", data)
        elif answer == 4:
            print('пока')
            break
        else:
            print("Повторите выбор")
