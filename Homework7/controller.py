import function
import view
import UI


def start():
    button=UI.menu()
    if button == 1:
        view.show(function.create_data())
        start()  # чтобы была опция выбора "сохранить в файл" после генерации
    elif button == 2:
        view.show(function.get_data())
    elif button == 3:
                function.save_data()
    elif button == 4:
        print('до свидания')
    else:
        print('выберите цифру из меню')
        start()


start()
