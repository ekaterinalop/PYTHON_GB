def create_data():
    import random
    from datetime import date
    global id
    global name
    global birthdate
    global phone1
    global phone2
    id = []
    name = []
    birthdate = []
    phone1 = []
    phone2 = []
    n = int(input('Введите размер справочника в тысячах строк (например 2)'))
    for i in range(n*1):  # исправить размерность на 1000
        id.append(i)
        name.append('user'+str(i))
        birthdate.append(date.today().replace(day=random.randint(
            1, 28), month=random.randint(1, 12), year=random.randint(1960, 2022)))
        phone1.append(random.randint(1000, 9999))
        phone2.append(random.randint(10000000, 99999999))
    return (id, name, birthdate, phone1, phone2)


def save_data():
    global id
    global name
    global birthdate
    global phone1
    global phone2
    
    with open('result_download.csv', 'w') as file:  # для такого формата записи не нужно делать close file
        for i in id:
            file.writelines(str(id[i])+" "+name[i]+" "+str(birthdate[i])+" "
                            + str(phone1[i])+" "+str(phone2[i])+"\n")


def get_data():
    global id
    global name
    global birthdate
    global phone1
    global phone2

    id = []
    name = []
    birthdate = []
    phone1 = []
    phone2 = []
    data = open('result_upload.csv', 'r')
    for line in data:

        items = []
        items = line.split()

        id.append(int(items[0]))
        name.append(items[1])
        birthdate.append(items[2])
        phone1.append(items[3])
        phone2.append(items[4])
    data.close()
    return (id, name, birthdate, phone1, phone2)



#import view
#create_data()
# get_data()
#save_data()
#print(id, name, birthdate, phone1, phone2)
# view.show(id,name,birthdate,phone1,phone2)
