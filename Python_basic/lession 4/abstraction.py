# ------------------------ lession 4 abstraction ------------------------------

# class Core:
#     def __init__(self) -> None:
#         self._type = {
#             'A': 100,
#             'B': 200
#         }

#     def get_selary(self, class_name):
#         return self._type.get(class_name, 0)


# class AccountingInterface:
#     def __init__(self, data) -> None:
#         self._core = Core()
#         self._database = data

#     def get_salary(self, name):
#         class_of_employee = self._database.get(name)
#         salary = self._core.get_selary(class_of_employee)
#         return salary

# db = {'Ivan': 'A', 'Maxsim': 'B'}

# a = AccountingInterface(db)
# print(a.get_salary('Ivan'))
# print(a.get_salary('Alexey'))


# class Parser:
#     def __init__(self) -> None:
#         pass

#     @staticmethod
#     def __convert_type(value_str):
#         result = 0
#         if isinstance(value_str, str):
#             if '.' in value_str:
#                 result = float(value_str)
#             else:
#                 result = int(value_str)
#         return result

#     def parse(self, expression):
#         packed_values = tuple(expression.split(' '))
#         if len(packed_values) < 3:
#             print("Worning identation, too few values")
#             return 0, 0, '+'
#         elif len(packed_values) > 3:
#             print("Worning identation, too many values")
#             return 0, 0, '+'
#         else:
#             a, op, b = packed_values
#             return self.__convert_type(a), self.__convert_type(b), op

# class Core:
#     def __init__(self) -> None:
#         self._parser = Parser()
#         self._functions = {
#             "+": lambda a, b: a + b,
#             "-": lambda a, b: a - b,
#             "*": lambda a, b: a * b,
#             "/": lambda a, b: a / b
#         }

#     def calculate(self, expression):
#         a, b, op = self._parser.parse(expression)
#         result = self._functions.get(op)(a, b)
#         return result


# class Interfase:
#     def __init__(self) -> None:
#         self._core = Core()
    
#     def run_calculator(self):
#         while True:
#             print('Enter your expression: eg. "2 + 2"')
#             expression = input()
#             result = self._core.calculate(expression)
#             print(f"Result: {result}")
#             print('==' * 10)

# if __name__ == "__main__":
#     calculator = Interfase()
#     calculator.run_calculator()


# ------------------------ homework abstraction -------------------------------

# 1. Организуйте архитектуру приложения “База данных” (псевдо). В роли базы данных у вас
# будет класс Database, который будет хранить данные в виде переменной списка.
# 2. Класс Database должен иметь методы read_data(criteria), write_data(element).
# 3. Для элемента данных напишите класс Data. В данном случае мы будем хранить данные о
# пользователях. Data будет иметь атрибуты: country, name, age, gender, height, weight.
# 4. В классе Database метод read_data будет принимать на вход аргумент criteria, который
# является словарем вида {“age”: 25}, после чего метод вернет отдельный список всех
# элементов у которых данное условие истино.
# Подсказка: чтобы получить у объекта класса значение его атрибута как у словаря, используйте
# следующий синтаксис: your_class_instance.__dict__.get(‘name’).
# PS: организуйте правильную инкапсуляцию. Вы должны добавлять элементы в класс Database
# только через метод write, но никак не напрямую через атрибут elements.

class Database:
    def __init__(self, DATABASE_LIST) -> None:
        self._DATABASE_LIST = DATABASE_LIST

    def read_date(self, criteria):
        pass
    
    def write_data(self, DATABASE_LIST, element):
        DATABASE_LIST.append(element)

class Data:
    def __init__(self, country, name, age, gender, height, weight) -> None:
        self._country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height 
        self.weight = weight

    def data(self, country, name, age, gender, height, weight):
        element = [country, name, age, gender, height, weight]
        return element

d = Database.write_data(element=('Ukraina', 'Ivan', 25, 'man', 170, 70))
