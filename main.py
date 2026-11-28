import visualLayer

if __name__ == '__main__':
    while True:

        print("Действия: ")
        print("0 - выход из программы")
        print("1 - добавить комнату: ")
        print("2 - удалить комнату")
        print("3 - показать список комнат")
        print("4 - забронировать комнату")
        print("5 - снять бронь на комнату\n")
        user_choice = input("Введите действие: ")
        try:
            if user_choice == "0":
                print("Выход из программы")
                break
            elif user_choice == "1":
                max_people = int(input("Введите максимальное количество человек в комнате: "))
                visualLayer.append_meeting_room(max_people)
            elif user_choice == "2":
                number_of_room = int(input("Введите номер комнаты для удаления: "))
                visualLayer.delete_room(number_of_room)
            elif user_choice == "3":
                visualLayer.show_rooms()
            elif user_choice == "4":
                number_of_room = int(input("Введите номер комнаты для брони: "))
                time_from = str(input("Введите время начала брони в формате ГГГГ:ММ:ДД ЧЧ:ММ :"))
                time_to = str(input("Введите время конца брони в формате ГГГГ:ММ:ДД ЧЧ:ММ :"))
                number_of_people = int(input("Введите количество людей: "))
                visualLayer.book_room(number_of_room, time_from, time_to, number_of_people)
            elif user_choice == "5":
                number_of_room = int(input("Введите номер забронированной комнаты для снятия брони: "))
                time_from = str(input("Введите время начала брони в формате ГГГГ:ММ:ДД ЧЧ:ММ :"))
                time_to = str(input("Введите время конца брони в формате ГГГГ:ММ:ДД ЧЧ:ММ :"))
                visualLayer.unbook_room(number_of_room, time_from, time_to)
            else:
                print("Выбрано несуществующее действие")
                print("")
        except ValueError as error:
            print(error)


