#класс самой комнаты
class Peregovorka:
    def __init__(self, max_people):
        if self.max_people <= 0:
            raise ValueError("Отрицательное количество людей в переговорке")
        self.max_people = max_people
        self.freedom = 1 #0 - свободна

    def capacity(self):
        return self.max_people

    def is_free(self):
        return self.freedom

    def change_free(self):
        if self.freedom == 1:
            self.freedom = 0
        if self.freedom == 0:
            self.freedom = 1

#класс отвечает распределение комнат и выдача свободных
class spisokPerigovorok:
    def __init__(self):
        self.peregovorki = []
    def add_room(self, peregovorka):
        self.peregovorki.append(peregovorka)
    def is_room_for(self, number_of_people):
        is_room = 0
        #алгоритм выбора и распределения можно доработать
        for i in range(len(self.peregovorki)):
            if self.peregovorki[i].capacity() >= number_of_people:
                if self.peregovorki[i].is_free() ==  1:
                    self.peregovorki[i].change_free()
                    is_room = i
                    return is_room+1
            else:
                return "Нет свободной комнаты"
    def people_leave_room(self, number_room):
        if number_room not in range(1,len(self.peregovorki)):
            raise ValueError("Несуществующий номер переговорки")
        else:
            self.peregovorki[number_room-1].change_free()
            return 1
