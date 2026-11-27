from dataLayer import ListOfTimedMeetingRooms,TimedMeetingRooms
meeting_rooms = ListOfTimedMeetingRooms

def append_meeting_room(max_people):
    meeting_rooms.add_room((TimedMeetingRooms(max_people)))

# def delete_meeting_room():