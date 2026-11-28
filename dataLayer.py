import re
from datetime import datetime

#класс самой комнаты
class MeetingRooms:
    def __init__(self, max_people: int):
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
    def get_max_people(self):
        return self.max_people
    def get_freedom(self):
        return self.freedom

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
            time_from = datetime.strptime(time_from, "%Y:%m:%d %H:%M")
        except ValueError:
            raise ValueError("Несуществующее время")

        #проверка времени до на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}", time_to):
            raise ValueError("Неверный формат времени")
        try:
            time_to = datetime.strptime(time_to, "%Y:%m:%d %H:%M")
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

        if not self.is_free_for_people(people, time_from,time_to):
            raise ValueError("Вы указали недоступное время")
        time_to = datetime.strptime(time_to, "%Y:%m:%d %H:%M")
        time_from = datetime.strptime(time_from, "%Y:%m:%d %H:%M")
        if len(self.booked_time) == 0:
            self.booked_time += [time_from, time_to]
            return 1
        if self.booked_time[-1] < time_from:
            self.booked_time += [time_from, time_to]
            return 1
        if self.booked_time[0] > time_to:
            self.booked_time[:0] = [time_from, time_to]
            return 1
        for index in range(2, len(self.booked_time), 2):
            if self.booked_time[index - 1] < time_from and time_to < self.booked_time[index + 1]:
                self.booked_time[index:index] = [time_from, time_to]
                return 1
        raise ValueError("Указанное время недоступно, но проверка на доступность сказала обратное")

    def unbook_room(self, time_from, time_to):
        #проверка времени c на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}",time_from):
            raise ValueError("Неверный формат времени")
        try:
            time_from = datetime.strptime(time_from, "%Y:%m:%d %H:%M")
        except ValueError:
            raise ValueError("Несуществующее время")
        #проверка времени до на корректность
        if not re.fullmatch(r"\d{4}:\d{2}:\d{2}\s\d{2}:\d{2}", time_to):
            raise ValueError("Неверный формат времени")
        try:
            time_to = datetime.strptime(time_to, "%Y:%m:%d %H:%M")
        except ValueError:
            raise ValueError("Несуществующее время")
        #время до должно быть меньше времени после
        if time_from > time_to:
            raise ValueError("Бронь начинается раньше, чем заканчивается")
        #время до не должно быть равно времени после
        if time_from == time_to:
            raise ValueError("Промежуток времени равен нулю")
        for index in range(0,len(self.booked_time),2):
            if time_from == self.booked_time[index] and time_to == self.booked_time[index+1]:
                self.booked_time = self.booked_time[:index]+self.booked_time[index+2:]
                return 1

        raise ValueError("Бронь отсутствует, попытка удалить несуществующую бронь")

    def get_booked_time(self):
        return self.booked_time

#класс отвечает за бронь комнат и хранение бронированных комнат
class ListOfTimedMeetingRooms:
    def __init__(self):
        self.rooms = []

    def add_room(self, timed_meeting_room : TimedMeetingRooms):
        self.rooms.append(timed_meeting_room)

    def delete_room(self, number_of_room : int):
        room = self.rooms[number_of_room-1]
        if len(room.get_booked_time()) != 0:
            raise ValueError("Попытка удалить забронированную комнату")
        self.rooms.remove(room)

    def find_room(self, number_of_people: int, time_from: str, time_to: str):
        for i in range(len(self.rooms)):
            room = self.rooms[i]
            if room.is_free_for_people(number_of_people,time_from,time_to):
                return i+1
        return 0

    def book_room(self, number_of_people: int, time_from: str, time_to: str, number_of_room: int):
        if number_of_room not in range(1, len(self.rooms)+1):
            raise ValueError("Несуществующий номер переговорки")
        room = self.rooms[number_of_room-1]
        if not room.is_free_for_people(number_of_people,time_from,time_to):
            raise ValueError("Выбрана недоступная комната")
        room.book_room(number_of_people,time_from,time_to)


    def unbook_room(self, time_from: str, time_to: str, number_of_room: int):
        if number_of_room not in range(1, len(self.rooms)+1):
            raise ValueError("Несуществующий номер переговорки")
        self.rooms[number_of_room-1].unbook_room(time_from,time_to)

    def get_rooms(self):
        return self.rooms

