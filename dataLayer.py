import re
from datetime import datetime

#класс самой комнаты
class MeetingRooms:
    def __init__(self, max_people):
        if max_people <= 0:
            raise ValueError("Не положительное количество людей в переговорке")
        self.max_people = max_people
        self.freedom = 1 #1 - свободна

    def is_free_for_people(self, people):
        return self.freedom and people <= self.max_people

    def change_free(self):
        if self.freedom == 1:
            self.freedom = 0
        if self.freedom == 0:
            self.freedom = 1

class TimedMeetingRooms(MeetingRooms):
    def __init__(self,max_people):
        super().__init__(max_people)
        self.booked_time = []
    def is_free_for_people(self, people,time_from=None,time_to=None):
        #если нет аргументов - вызываем старый метод класса
        if time_from is None and time_to is None:
            return super().is_free_for_people(people)
        elif time_from is None or time_to is None:
            return ValueError("Передано одно время вместо промежутка, бронь невозможна")

        #проверка времени c на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}",time_from):
            return ValueError("Неверный формат времени")
        try:
            time_from = datetime.strptime(time_from, "%Y:%m:%d %H:%D")
        except ValueError:
            return ValueError("Несуществующее время")

        #проверка времени до на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}", time_to):
            return ValueError("Неверный формат времени")
        try:
            time_to = datetime.strptime(time_to, "%Y:%m:%d %H:%D")
        except ValueError:
            return ValueError("Несуществующее время")

        #время до должно быть меньше времени после
        if time_from > time_to:
            return ValueError("Бронь начинается раньше, чем заканчивается")
        #время до не должно быть равно времени после
        if time_from == time_to:
            return ValueError("Промежуток времени равен нулю")

        #ЗДЕСЬ НАДО РЕАЛИЗОВАТЬ САМУ БРОНЬ
        if super().is_free_for_people(people):
            pass


#класс отвечает распределение комнат и выдачу свободных
class ListOfMeetingRooms:
    def __init__(self):
        self.list_of_meeting_rooms = []

    def add_room(self, meeting_room):
        self.list_of_meeting_rooms.append(meeting_room)

    def delete_room(self, number_of_room):
        room = self.list_of_meeting_rooms[number_of_room-1]
        if number_of_room not in range(1,len(self.list_of_meeting_rooms)):
            raise ValueError("Несуществующий номер переговорки")
        else:
            if room.is_free_for_people(1):
                del room

    def find_room_for_people(self, number_of_people):
        #алгоритм выбора и распределения можно доработать
        for i in range(len(self.list_of_meeting_rooms)):
            room = self.list_of_meeting_rooms[i]
            if room.is_free_for_people(number_of_people) ==  1:
                return i+1
        return "Нет свободной комнаты"

    def change_status_room_n(self, number_room):
        if number_room not in range(1,len(self.list_of_meeting_rooms)):
            raise ValueError("Несуществующий номер переговорки")
        else:
            self.list_of_meeting_rooms[number_room-1].change_free()
            return 1
