class Element():
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    def data_sort(self):
        global data
        #шейкерная сортировка
        start = 0
        end = len(data) - 1

        while True:
            swap = False
            for i in range(start, end):
                current_element = data[i]
                next_element = data[i + 1]
                if current_element.priority < next_element.priority:
                    data[i] = next_element
                    data[i + 1] = current_element
                    swap = True
            
            end -= 1
            if swap == False:
                break
            swap = False
            for i in range(end, start, -1):
                current_element = data[i]
                next_element = data[i - 1]
                if current_element.priority > next_element.priority:
                    data[i] = next_element
                    data[i - 1] = current_element
                    swap = True
            start += 1
            if swap == False:
                break
        return data
    def show_data(self):
        global data
        for i in data:
            print("Фамилия: ", i.value)
            print("Приоритет: ", i.priority)
    def delete_element(self, value):
        for element in data:
            if element.value == value:
                data.remove(element)

data = []
while True:
    menu = int(input("Выберите действие:\n1.Добавить фамилию в очередь\n2.Посмотреть очередь\n3.Удалить фамилию из очереди "))
    if menu == 1:
        value = str(input("Введите фамилию "))
        priority = int(input("Введите приоритет "))
        element = Element(value, priority)
        data.append(element)
        data = element.data_sort()
    elif menu == 2:
        element.show_data()
    elif menu == 3:
        value = str(input("Введите фамилию, которую хотите удалить из очереди "))
        element.delete_element(value)
