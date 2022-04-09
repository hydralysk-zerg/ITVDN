# ---------------------------lesssons Class part 1 --------------------------------------
# 
# class Human:
#     def __init__(self, age, name, gender):
#         self.age = age
#         self.name = name
#         self.gender = gender
    
    
#     def get_name(self):
#         return self.name
    
    
#     def get_age(self):
#         return self.age
    
    
#     def get_gender(self):
#         return self.gender
    
    
#     def get_age_and_name(self):
        # return self.age, self.get_name()


# human_1 = Human(name = "Jon Smit", age = 25, gender='man')
# print('Agent', human_1.name, 'age', human_1.age, 'gender', human_1.gender)
# print(human_1.name)
# print(human_1.age)
# print(human_1.gender)

# print(human_1.get_name())
# print(human_1.get_age())
# print('gender',human_1.get_gender())
# print(human_1.get_age_and_name())

# ----------------------------Part 2 -------------------------------------

# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
    

# c = C()
# print(c.a, c.b)
# print(c.b)

# ---------------------------------- TASK's --------------------------------------

# class MyCar:
#     def __init__(self, brand, color, engine_capacity):
#         self.brand = brand
#         self.color = color
#         self.engine_capacity = engine_capacity
    
#     @staticmethod
#     def drive_forward():
#         print('Drive forward')

#     @staticmethod
#     def drive_back():
#         print('Drive back')


# my_car = MyCar(brand="Mazda", color='Red', engine_capacity=2.5)
# print(f'My car {my_car.brand} color {my_car.color} engine capacity {my_car.engine_capacity} litra')
# my_car.drive_forward()
# my_car.drive_back()

# class UpdateMyCar(MyCar):

#     @staticmethod
#     def left_turn():
#         print('Left turn')

#     @staticmethod
#     def right_turn():
#         print('Right turn')


# update_my_car = UpdateMyCar(brand='Toyota', color='Black', engine_capacity=4)
# print(f'My new car {update_my_car.brand} color {update_my_car.color} engine capacity {update_my_car.engine_capacity} litra')
# update_my_car.drive_back()
# update_my_car.drive_forward()
# update_my_car.left_turn()
# update_my_car.right_turn()
# UpdateMyCar.right_turn()


# class Airplane:
#     def __init__(self, airplan_brand):
#         self.airplan_brand = airplan_brand
    
#     @staticmethod
#     def take_off():
#         print('Take off')



# airplane = Airplane(airplan_brand='Boing 747')
# print(f'Airplan brand {airplane.airplan_brand}')
# airplane.take_off()


# class Transport(UpdateMyCar, Airplane):
#     def __init__(self, brand, color, engine_capacity, airplan_brand):
#         UpdateMyCar.__init__(self, brand, color, engine_capacity)
#         Airplane.__init__(self, airplan_brand)


# transport = Transport(brand='BMW', color='Blue', engine_capacity=0.7, airplan_brand="F15")
# print(f'{transport.airplan_brand} {transport.brand} {transport.color} {transport.engine_capacity}')
# transport.take_off()
# transport.drive_forward()
# transport.left_turn()
# transport.right_turn()
# transport.drive_back()


# ---------------------------- Homework -------------------------------------------

# Написать класс Cat, создать ему атрибуты size, color, cat_type.
# 2. При создании объекта класса передавать в конструктор color и cat_type, которые
# записываются в соответсвующие атрибуты.
# 3. Сделать метод set_size, в котором если self.cat_type это “indoor”, то self.size = ‘small’ иначе
# self.size=’undefined’. Протестируйте разные варианты.
# 4. Сделать класс Tiger, унаследованный от класса Cat.
# 5. Переопределить метод set_size таким образом чтобы если self.cat_type это ‘wild’, то self.size
# = ‘big’ иначе self.size=’undefined’.
class Cat:
    def __init__(self, size, color, cat_type) -> None:
        self.size = size
        self.color = color
        self.cat_type = cat_type


    def color_and_type(self):
        return self.color, self.cat_type


    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
            return self.size
        else:
            self.size = 'undefined'
            return self.size


cat = Cat(size='big', color='orange', cat_type='indoor')
print(cat.set_size())

class Tiger(Cat):
    def __init__(self, size, color, cat_type):
        super().__init__(size, color, cat_type)

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
            return self.size
        else:
            self.size = 'undefined'
            return self.size

tiger = Tiger(size='small', color='orange', cat_type='wilda')
print(tiger.set_size())