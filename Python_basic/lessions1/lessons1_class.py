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

import re


# ----------------------------Part 2 -------------------------------------

class Human:
    def __init__(self, age):
        self.age = age

    def my_age(self):
        return self.age, print(f"My age {Human.my_age()}")

human = Human(age=35)
human.my_age()

        