#класс самой комнаты
class MeetingRooms:
    def __init__(self, max_people):
        if self.max_people <= 0:
            raise ValueError("Отрицательное количество людей в переговорке")
        self.max_people = max_people
        self.freedom = 1 #1 - свободна

    def capacity(self):
        return self.max_people

    def is_free(self):
        return self.freedom

    def change_free(self):
        if self.freedom == 1:
            self.freedom = 0
        if self.freedom == 0:
            self.freedom = 1

#класс отвечает распределение комнат и выдачу свободных
class ListOfMeetingRooms:
    def __init__(self):
        self.list_of_meeting_rooms = []
    def add_room(self, meeting_room):
        self.list_of_meeting_rooms.append(meeting_room)
    def is_room_for(self, number_of_people):
        #алгоритм выбора и распределения можно доработать
        for i in range(len(self.list_of_meeting_rooms)):
            if self.list_of_meeting_rooms[i].capacity() >= number_of_people:
                if self.list_of_meeting_rooms[i].is_free() ==  1:
                    self.list_of_meeting_rooms[i].change_free()
                    return i+1
        return "Нет свободной комнаты"
    def people_leave_room(self, number_room):
        if number_room not in range(1,len(self.list_of_meeting_rooms)):
            raise ValueError("Несуществующий номер переговорки")
        else:
            self.list_of_meeting_rooms[number_room-1].change_free()
            return 1
