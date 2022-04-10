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

class Worker:
    RIGHTS = 'Equal'
    SALARY_CLASS = {
            'A': 100,
            'B': 200,
            'C': 300
        }
    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)
    
    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_CLASS.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary

w = Worker(working_class='B')
print(w.salary)