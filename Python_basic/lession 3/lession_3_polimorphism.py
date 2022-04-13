# --------------------- lession 3 polinorphism -----------------------------

# ---------------------------  overload -----------------------------

# class Base:
#     def __init__(self, a) -> None:
#         self.__a = a

#     def print_a(self, square = False, multiplaer = None):
#         if square and not multiplaer:
#             print(self.__a ** 2)
#         elif not square and multiplaer:
#             print(self.__a * multiplaer)
#         elif square and multiplaer:
#             print((self.__a ** 2) * multiplaer)
#         else:
#             print(self.__a)


# base =  Base(5)
# base.print_a(square=True)
# base.print_a(multiplaer=2)
# base.print_a(square=True, multiplaer=2)
# base.print_a()

# class Car:
#     def __init__(self, name) -> None:
#         self._speed_name_map = {
#             'BMW': 250,
#             'Mersedes': 300,
#             'Toyota': 320
#         }
#         self._max_speed = self._define_max_speed(name)

#     def _define_max_speed(self, name):
#         return self._speed_name_map.get(name, 0)

#     def distance_on_max_speed(self, distance):
#         if self._max_speed == 0:
#             print(f'Speed = 0, select valid car brand: {tuple(self._speed_name_map.keys())}')
#             return 0
#         return distance / self._max_speed


# carB = Car('BMW')
# carM = Car('Mersedes')
# carT = Car('Toyota')
# carNotName = Car('Not name')

# print(carB.distance_on_max_speed(300))
# print(carM.distance_on_max_speed(300))
# print(carT.distance_on_max_speed(300))
# print(carNotName.distance_on_max_speed(300))

# class Animal:
#     def __init__(self, name) -> None:
#         self._nane = name

#     def voice(self):
#         if self._nane == 'cat':
#             print('meow')
#         elif self._nane == 'dog':
#             print('bark')
#         else:
#             print('@ # $ % ^ & *')


# a = Animal('cat')
# a1 = Animal('dog')
# a2 = Animal('elephant')

# a.voice()
# a1.voice()
# a2.voice()

# ------------------------------ redefinition -----------------------------

# class Multiplaer:
#     def __init__(self, a) -> None:
#         self._a = a

#     def print_a(self, x):
#         print(self._a * x)


# m = Multiplaer(5)
# m.print_a(4)

# class Exponent(Multiplaer):
#     def print_a(self, x):
#         print(self._a ** x)


# e = Exponent(7)
# e.print_a(2)

# class Animal:
#     def __init__(self, name) -> None:
#         self._name = name

#     def voice(self):
#         print('Grrrr')


# class Dog(Animal):
#     def voice(self):
#         print('Bark')


# class Cat(Animal):
#     def voice(self):
#         print('Meow')


# a = Animal('Dino')
# a.voice()

# d = Dog("bobik")
# d.voice()

# c = Cat('barsik')
# c.voice()


# class Parallelogram:
#     def __init__(self, width, length) -> None:
#         self._width = width
#         self._length = length

#     def get_area(self):
#         return self._width * self._length

# class Square(Parallelogram):
#     def get_area(self):
#         return self._width * self._width
        

# p = Parallelogram(5, 5)
# print(p.get_area())
# s = Square(56, 4)
# print(s.get_area())

# def function(data, new_value):
#     if isinstance(data, list):
#         data.append(new_value)
#     elif isinstance(data, set):
#         data.add(new_value)
#     elif isinstance(data, str):
#         if isinstance(new_value, str):
#             data += new_value
#     return data

# print(function('{1, 5, 3}', '4'))

# ------------------------------ homework -----------------------------

# 1. Написать класс User, у него будут в конструкторе определяться поля age, name, user_type,
# а метод будет access_database.
# 2. Сделать метод таким, чтобы если self.user_type был равен “superuser”, то метод выводил в
# консоль “access granted”, в случае если это просто юзер, то выводило “access denied”.
# 3. Для суперюзера сделать унаследованный класс SuperUser от User.

class User:
    def __init__(self, age, name, user_type) -> None:
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == 'superuser':
            print('access granted')
        elif self.user_type == 'user':
            print('access denied')
        else:
            print('you not user!!')
        
u = User(34, 'Ivan', 'super')
u.access_database()

class SuperUser(User):
    def __init__(self, age, name, user_type):
        super().__init__(age, name, user_type)

s = SuperUser(45, 'BoB', 'superuser')
s.access_database()