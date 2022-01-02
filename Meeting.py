from User import User
from AutoRepairShop import AutoRepairShop



class Meeting(User, AutoRepairShop): # Тут сlass Meeting наследует родителей User и AutoRepairShop что бы иметь доступ к его аргументам и методам
    def __init__(self, name, usercarmodel, users, carname, cars, meeting=list()):
        self.__name = name
        self.__usercarmodel = usercarmodel
        self.users = users
        self.__company_name = carname
        self.cars = cars
        self.__meeting = meeting


    def _AddMeetingInArray(self, name, usercarmodel, carname, time): #Метод для добавления встречи принимает 4 параметра (Вводится в ручную)
        mas = list()
        for i in self.users.__iter__():
            if name == i[0]:
                mas.append(name)
                mas.append(usercarmodel)

        for i in self.cars.__iter__():
            if carname == i[1]:
                mas.append(carname)

        mas.append(time)

        self.__meeting.append(mas)
        print("\n A meeting {} with auto repair shop {} was created".format(name,carname))

    def PrintMeeting(self): #Метод для вывода встреч в красивом виде
        for i in self.__meeting.__iter__():
            print('\n Name: {}\n Car model: {}\n Company name: {}\n Time: {}\n'.format(i[0], i[1], i[2], i[3]))

    def _removeMeeting(self, name): #Метод удаление встречи,принимает один параметр
        for i in self.__meeting.__iter__():
            if name == i[0]:
                self.__meeting.remove(i)
                print("A meeting {}".format(name) + ' deleted')

    def _ChangeTimeMeeting(self, namemet, newtime):  #Метод изменение времени,получает два параметра (Вводится в ручную)
        for i in self.__meeting.__iter__():
            if namemet == i[0]:
                i[2] = newtime
