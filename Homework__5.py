import dataclasses
import collections

#1

class Laptop:
    def __init__(self, name_laptop, model_laptop, type_battery, capacity_battery):
        self.name_laptop = name_laptop
        self.model_laptop = model_laptop
        self.laptop_battery = Battery(type_battery, capacity_battery)

    def __str__(self):
        return f'{self.name_laptop}, {self.model_laptop}, with {self.laptop_battery}'


class Battery:
    def __init__(self, type_battery, capacity_battery):
        self.type_battery = type_battery
        self.capacity_battery = capacity_battery

    def __str__(self):
        return f'{self.type_battery}, {self.capacity_battery}'

apple = Laptop('Apple', 'MacBook Pro 16', 'Lithium-polymer ' 'battery', 'capacity:' '100 wt')
print(apple)

#2

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string

class String:
    def __init__(self, type_string):
        self.type_string = type_string

string = String('Nylon ')
guitar = Guitar(string)

#3

class Calc:
    @staticmethod
    def add_num(a, b, c):
        return a + b + c


num = Calc()
print(Calc.add_num(9, 19, 7))

#4

class Pasta:
    Carbonara_ingrediente = ['Forcemeat', 'Tomatoes']
    Bolognaise_ingrediente = ['Bacon', 'Parmesan', 'Eggs']

    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    @classmethod
    def Carbonara(cls):
        return Pasta(cls.Carbonara_ingrediente)

    @classmethod
    def Bolognaise(cls):
        return Pasta(cls.Bolognaise_ingrediente)

pasta_1 = Pasta.Carbonara()
print(f'Pasta  Carbonara, ingrediente: {pasta_1.ingrediente}')
pasta_2 = Pasta.Bolognaise()
print(f'Pasta Bolognaise, ingrediente: {pasta_2.ingrediente}')


#5

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert = Concert()
Concert.max_visitors_num = 50
concert.visitors_count = 1000
print(concert.visitors_count)

#6

@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    mail: str
    birthday: str
    age: int

user = AddressBookDataClass(9, 'Carl Johnson', '9339992', 'Grove Street', 'CJJohnson@gmail.com', '1968', 53 )
print(user)

#7

AddressBookDataClass = collections.namedtuple('user', ['key', 'name', 'phone_number', 'address', 'mail', 'birthday', 'age'])
user = AddressBookDataClass(9, 'Carl Johnson', '9339992', 'Grove Street', 'CJJohnson@gmail.com', '1968', 53 )
print(user)


#8

class AddressBook:
    def __init__(self, key, name, phone_number, address, mail, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.mail = mail
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook (key = {self.key}, name = {self.name}, phone_number = {self.phone_number},' \
               f'address = {self.address}, mail = {self.mail}, birthday = {self.birthday}, age = {self.age}'

next_user = AddressBook(9, 'Carl Johnson', '9339992', 'Grove Street', 'CJJohnson@gmail.com', '1968', 53 )
print(next_user)

#9

class Person:
    name = 'John'
    age = 36
    country = "USA"


user = Person
user.age = 33
print(user.age)

#10

class Student:
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self. name = name


student = Student(9798, 'Fil')
setattr(student, 'mail', 'Fil@gmail.com')
student.mail = 'ManCityFil@gmail.com'
student_mail = getattr(student, 'mail')
print(student_mail)

#11

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    @property
    def temperature(self):
        return  (self._temperature * 1.8) + 32

temp = Celsius(36)
print(temp.temperature)
