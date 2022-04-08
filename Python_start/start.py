# lesion 9 function part 2
# Задание 1
# Напишите функцию, которая меняет значение глобальной переменной.

# x = 1
# def change_global():
#     global x 
#     x = 15
#     return x


# z = change_global()
# print(z)

# Задание 2
# Напишите рекурсивную функцию для того, чтобы посчитать значения факториала числа, которое
# передается аргументом (см. рекомендуемые ресурсы).:

# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n * factorial(n - 1)

# x = factorial(6)
# print(x)

# Применить встроенные функции на практике на своем примере.
# Задание 3
# Найдите наибольшее значение в списке с помощью рекурсии.

# def recyrsiya(list_recursiya):    
#     return max(list_recursiya), min(list_recursiya)

# y = recyrsiya([0, 1, -55, 15, 74, 27, 22, 46, 85, 36, 59, 75])
# print(y)

# lesson 10 try-except-finally
# Задание 1
# Написать функцию, которая принимает параметрами 2 аргумента и возвращает результатом их
# частное, где первый аргумент - делимое, а второй - делитель (первый разделить на второй).
# Обработать ZeroDivizionError, вернуть 0 и вывести сообщение об ошибке что на 0 делить нельзя.

# def not_zero_division(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as error:
#         return error, "i's not division in zero"


# x = not_zero_division(5, 0)
# print(x)

# Задание 2
# Написать функцию, которая возвращает элемент из списка по индексу. Принимает 2 аргумента:
# список и индекс. Написать обработку исключения - если в списке такого индекса нету, вывести
# сообщение об ошибке и вернуть -1.



# def return_list_index():
#     print('+')


# return_list_index.add_arg(x)

# if x != None:
#     print(str(x[0])+'.', "Value defolt:", x[1])



