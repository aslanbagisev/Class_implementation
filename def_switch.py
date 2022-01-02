from User import User
from AutoRepairShop import AutoRepairShop
from Meeting import Meeting


u = User('', '', '', '', '')
c = AutoRepairShop('', '', '', '', '')
m = Meeting('','', u.users, '', c.cars)



def quit(): #Функцию выходит из программы
    print("Thanks for testing my program")
    exit(0)

def adduser():  #Функцию добавление пользователя
    u = User(input(' Enter name: '), input(' Enter email: '), input(' Enter city: '), input(' Enter postal code: '),
             input(' Enter country: '))
    u._addUserInArray()

def removeuser(): #Функцию удаление пользователя
   u._removeUser(input(' Enter name for delete: '))

def User_Conclusion(): #Функцию вывода всех пользователей
    u.Print()

def Addingaworkshop(): #Функцию добавления автомастерской
    c = AutoRepairShop(input(' Enter company name: '), input(' Enter car mark: '), input(' Enter city: '),
                       input(' Enter postal code: '),
                       input(' Enter country: '))
    c._addCarInArray()

def Carworkshopremoval(): #Функцию удаления автомастерской
    c._removeCar(input(' Enter company name for delete: '))

def Conclusion_of_auto_repair_shops(): #Функцию вывода всех автомастерских
    c.PrintCar()

def Searchastomaster_workshops_by_city(): #Функцию поиска австомастерских в конкретном городе
    c.findCar(input(' Enter city for find all autorepairshop: '))

def car_workshop_meeting(): #Функцию создания встречи
    m._AddMeetingInArray(input(' Enter username: '),input(' User Car model: '),input(' Enter company name: '),
                        time=input(' Enter date for meeting: '))

def Delete_appointment(): #Функцию удаление встречи
    m._removeMeeting(input(' Enter date for remove meeting: '))

def change_meeting_time(): #Функцию изменение времени для встречи
    m._ChangeTimeMeeting(input(" Enter the name (User): "), input(" Enter a new meeting time:"))

def conclusion_meetings():
    m.PrintMeeting()


