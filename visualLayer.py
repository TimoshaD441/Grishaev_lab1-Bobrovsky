from dataLayer import ListOfTimedMeetingRooms,TimedMeetingRooms
meeting_rooms = ListOfTimedMeetingRooms()

def append_meeting_room(max_people: int):
    meeting_rooms.add_room(TimedMeetingRooms(max_people))

# def delete_meeting_room():

def show_rooms():
    rooms = meeting_rooms.get_rooms()
    for index_room in range(len(rooms)):
        room = rooms[index_room]
        print(f"Комната номер {index_room+1}: ")
        print("Вместимость комнаты: ", room.get_max_people())
        booked_time = room.get_booked_time()
        if len(booked_time) ==  0:
            print("Комната свободна на любое время")
        else:
            print("Комната забронированна на следующие промежутки времени: ")
            for index_time in range(0,len(booked_time),2):
                time_from = booked_time[index_time]
                time_to = booked_time[index_time+1]
                print("С ", time_from.strftime("%Y:%m:%d %H:%M"), " до ", time_to.strftime("%Y:%m:%d %H:%M"))
    print("")

def book_room(number_of_room: int, time_from: str, time_to: str, number_of_people: int):
    meeting_rooms.book_room(number_of_people,time_from,time_to,number_of_room)

def unbook_room(number_of_room: int, time_from: str, time_to: str):
    meeting_rooms.unbook_room(time_from, time_to,number_of_room)

def delete_room(number_of_room: int):
    meeting_rooms.delete_room(number_of_room)