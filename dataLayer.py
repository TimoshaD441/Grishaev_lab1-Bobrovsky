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
            raise ValueError("Передано одно время вместо промежутка, бронь невозможна")

        #проверка времени c на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}",time_from):
            raise ValueError("Неверный формат времени")
        try:
            time_from = datetime.strptime(time_from, "%Y:%m:%d %H:%D")
        except ValueError:
            raise ValueError("Несуществующее время")

        #проверка времени до на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}", time_to):
            raise ValueError("Неверный формат времени")
        try:
            time_to = datetime.strptime(time_to, "%Y:%m:%d %H:%D")
        except ValueError:
            raise ValueError("Несуществующее время")

        #время до должно быть меньше времени после
        if time_from > time_to:
            raise ValueError("Бронь начинается раньше, чем заканчивается")
        #время до не должно быть равно времени после
        if time_from == time_to:
            raise ValueError("Промежуток времени равен нулю")
        #сама проверка есть ли место по времени
        if super().is_free_for_people(people):
            if len(self.booked_time) == 0:
                return 1
            if self.booked_time[-1] < time_from:
                return 1
            if self.booked_time[0] > time_to:
                return 1
            for index in range(2,len(self.booked_time),2):
                if self.booked_time[index-1] < time_from and time_to < self.booked_time[index+1]:
                    return 1
        return 0

    def book_room(self, people, time_from, time_to):
        if not self.is_free_for_people(people, time_to,time_from):
            raise ValueError("Вы указали недоступное время")
        if len(self.booked_time) == 0:
            self.booked_time.append([time_from, time_to])
            return 1
        if self.booked_time[-1] < time_from:
            self.booked_time.append([time_from, time_to])
            return 1
        if self.booked_time[0] > time_to:
            self.booked_time[:0] = [time_from, time_to]
            return 1
        for index in range(2, len(self.booked_time), 2):
            if self.booked_time[index - 1] < time_from and time_to < self.booked_time[index + 1]:
                self.booked_time[index:index] = [time_from, time_to]
                return 1
        raise ValueError("Указанное время недоступно, но проверка на доступность сказала обратное")

    def what_time_is_booked(self):
        return self.booked_time

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
