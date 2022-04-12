# ----------------- lessone 2 encapsulation --------------------

#   value i's pablic properties
#  _value i's protected properties
# __value i's private properties


# class Test:
#     def __init__(self, test):
#         self.__private_test = test
    
#     def get_private_test(self):
#         return self.__private_test

#     @staticmethod
#     def __private_function():
#         print("I's private function")


#     def call_private(self):
#         return self.__private_function()

# test = Test(test=10)
# print(test.get_private_test())
# test.call_private()

# ----------------- get_ter and set_ter --------------------------

# class User:
#     def __init__(self, name):
#         self.__name = name

#     @property # getter
#     def name(self):
#         return self.__name
    
#     @name.setter # setter
#     def name(self, value):
#         self.__name = value


# user = User('Bob')
# user.name = 'Joaba'
# print(user.name)

# class Worker:
#     SALARY_CLASS = {
#             'A': 100,
#             'B': 200,
#             'C': 300
#         }
#     def __init__(self, working_class):
#         self.__salary = self.__get_salary(working_class)
    
#     @staticmethod
#     def __get_salary(working_class):
#         return Worker.SALARY_CLASS.get(working_class, 0)

#     @property
#     def salary(self):
#         return self.__salary

# w = Worker(working_class='B')
# print(w.salary)

# ------------------------- Task example ---------------------------

# class TextProcessor:
#     def __init__(self):
#         self._punctuation = ",#*&?;:`~"

#     def __is_punctuation(self, char):
#         return char in self._punctuation

#     def get_clean_string(self, text):
#         clean_text = ''
#         for char in text:
#             if self.__is_punctuation(char):
#                 continue
#             clean_text += char
#         return clean_text


# class TextLoader:
#     def __init__(self):
#         self.__text_processor = TextProcessor()
#         self.__clean_string = None

#     def set_clean_string(self, text):
#         self.__clean_string = self.__text_processor.get_clean_string(text)

#     @property
#     def clean_string(self):
#         print(f'Clean string is:{self.__clean_string}')
#         return self.__clean_string


# class DataInterface:
#     def __init__(self) -> None:
#         self.__text_loader = TextLoader()

#     def process_texts(self, texts):
#         clean_texts = []
#         for text in texts:
#             self.__text_loader.set_clean_string(text)
#             clean = self.__text_loader.clean_string
#             clean_texts.append(clean)
#         return clean_texts

# p = DataInterface()
# t = ['Hello, I am John', 'Hey, what is the weather today?']
# p.process_texts(t)

# ------------------------- Homework --------------------------------
# 1. Написать класс, который описывает пользователя (class User), сделать ему приватный
# атрибут age, который передается в конструктор, публичный атрибут name, который так же
# передается в конструктор.
# 2. Написать getter и setter для атрибута age.
# 3. Добавить в setter проверку на валидный возраст (не отрицательное, целое число).

class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value == int(value):
            if value > 0:
                self.__age = value
                print(f'I am {self.name} I am age {self.age}')
            else:
                print(f'Age {self.name} cannot be less than zero')
        else:
            print(f'Age {self.name} not integer')


u = User(age=0, name='Ivan')
u.age = 34
print(u.age, u.name)
