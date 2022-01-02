from def_switch import *


# ******************************#
#####Creator Bagishev Aslan#####
# ******************************#

def main():
    # Ниже я создал словарь который по ключам вызывает функции которые я разместил в файле def_switch и каждый ключ вызывает соотвествующую функцию в отличии от выбора пользователя
    while True:  # В отличии от выбора пользователя в словаре ищется ключ и при нахождении ключа он вызывает функцию из def_switch
        switcher = {
            0: quit,
            1: adduser,
            2: removeuser,
            3: User_Conclusion,
            4: Addingaworkshop,
            5: Carworkshopremoval,
            6: Conclusion_of_auto_repair_shops,
            7: Searchastomaster_workshops_by_city,
            8: car_workshop_meeting,
            9: Delete_appointment,
            10: change_meeting_time,
            11: conclusion_meetings,
        }

        def select(argument):
            func = switcher.get(argument, "nothing")
            return func()

        print(
            '\n 1) To add a user \t\t\t\t\t\t\t2) To delete a user\n 3) To display users \t\t\t\t\t\t4) To add a workshop\n'
            ' 5) To delete a workshop\t\t\t\t\t6) To display all workshops \n 7) To search for car services in the city\t8) Create an appointment with a car workshop\n 9) Delete appointment \t\t\t\t\t\t10) Change meeting time\n 11) View all meetings\t\t\t\t\t\t0) Exit\n')

        select(int(input(" Your choice: ")))  # Пользователь выбирает функцию которой он хочет воспользоваться


if __name__ == '__main__':
    main()
