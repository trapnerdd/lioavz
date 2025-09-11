import random

def task1():
    data = [0, 1, 2, 3, 4, 5]
    min_n = min(data)
    max_n = max(data)
    print("task1:", min_n - max_n)

def task2():
    data = []
    for i in range(10):
        i = random.randint(0, 10)
        data.append(i)
    print("task2:", data)

def task3():
    n = int(input('Введите длину массива: '))
    data = []
    for i in range(n):
        i = random.randint(0, 10)
        data.append(i)
    print("task3:", data)

def task4():
    data = [[1, 2, 3], [5, 4, 1]]
    print("task4 (массив):", data)
    for i in data:
        summ = 0
        for j in i:
            summ += j
        print("Сумма строки:", summ)

def task5():
    data = [
        {"Фамилия": 'Свинухов', "Имя": 'Колян', "Название факультета": 'ФВТ', "Номер зачетки": '24ВВВ213'},
        {"Фамилия": 'кузьмичев', "Имя": 'Саша', "Название факультета": 'ФВТ', "Номер зачетки": '24ВВВ212'},
        {"Фамилия": 'гришанин', "Имя": 'ваня', "Название факультета": 'ФВТ', "Номер зачетки": '24ВВВ214'},
        {"Фамилия": 'белоусов', "Имя": 'игорян', "Название факультета": 'ФВТ', "Номер зачетки": '24ВВВ216'},
        {"Фамилия": 'треглазов', "Имя": 'максим', "Название факультета": 'ФВТ', "Номер зачетки": '26ВВВ213'}
    ]
    while True:
        choice = int(input("\n1 - найти студента\n2 - добавить студента\n3 - вывести список студентов\n4 - завершить\nВаш выбор: "))
        if choice == 1:
            surname = str(input("Введите фамилию или номер зачетной книжки студента: "))
            output = False
            for s in data:
                if (s["Фамилия"].lower() == surname.lower()) or (s["Номер зачетки"].lower() == surname.lower()):
                    print(s)
                    output = True
            if not output:
                print("такого студента нет(((")
        elif choice == 2:
            z_n = str(input("Введите номер зачетной книжки студента: "))
            f = False
            for s in data:
                if (s["Номер зачетки"].lower() == z_n.lower()):
                    print("ошибка, такой студент уже есть")
                    f = True
            if not f:
                surname = str(input("Введите фамилию студента: "))
                name = str(input("Введите имя студента: "))
                f_name = str(input("Введите название факультета студента: "))
                data.append({"Фамилия": surname, "Имя": name, "Название факультета": f_name, "Номер зачетки": z_n})
                print("Студент добавлен")
        elif choice == 3:
            for i in data:
                print(i)
        elif choice == 4:
            break
        else:
            print("введите корректное значение")

def task6():
    n = int(input("Введите размер квадратного массива: "))
    data = [[random.randint(-20, 40) for _ in range(n)] for _ in range(n)]

    # Симметрия относительно главной диагонали
    for i in range(n):
        for j in range(i + 1, n):
            data[j][i] = data[i][j]

    print("\nСимметричный массив:")
    for row in data:
        print(row)

# Вызовы функций
# task5()  # эта задача интерактивная
task1()
task2()
task3()
task4()
task5()
