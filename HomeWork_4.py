#1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = mileage
        self.mileage = mileage


#2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.__seating_capacity = seating_capacity

    def seating_capacity(self):
        return self.__seating_capacity


#3
bus = Bus(90, 1200, 54)
print(type(bus))

print(isinstance(bus, Vehicle))

#4
print(isinstance(bus, Vehicle))

#5
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id


#6
class SchoolBus(School, Bus):
    def __init__(self, school_id, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.__bus_school_color = bus_school_color

    def bus_school_color(self):
        return self.__bus_school_color



print(issubclass(SchoolBus, Vehicle))


#7
class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Hrrr')


class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Hrrr')


bear = Bear('Barni', 1)
wolf = Wolf('BigBi', 5)

for animal in (bear, wolf):
    animal.make_sound()



#8
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print('Your city is too small.')

#9
    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


#10
class Count:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

a = Count(7)
b = Count(9)
c = a + b
print(c)

a_1 = Count(11)
b_1 = Count(4)
c_1 = a_1 + b_1
print(c_1)

#11

class CallSum:
    def __call__(self, *args):
        return sum(args)


result = CallSum()
print(result(9, 99, 999))


#12

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))