# ---------------------------------- recursion -------------------------------------
# a = [1, 2, 3, 4, 5]
# b = [56, 67, 3, 78, 890, 2]

# def iter_arr(array):
#     for element in array:
#         print(element)

# def iter_rec(array, index=0):
#     if index < len(array):
#         print(array[index])
#         index += 1
#         iter_rec(array, index)

# iter_rec(b)
# iter_arr(a)

# class Node:
#     def __init__(self, data) -> None:
#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

#     def search(self, data):
#         if data == self.data:
#             print(f'{data} in tree')
#             return True
#         if data < self.data:
#             if self.left is None:
#                 print(f'{data} not in tree')
#                 return False
#             return self.left.search(data)
#         if self.right is None:
#             print(f'{data} not in tree')
#             return False
#         return self.right.search(data)

#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.data)
#         if self.right:
#             self.right.print_tree()
#         # print(self.data)

# a = [23, 34, 19, 89, 987, 890, 45, 56]
# for i in range(len(a)):
#     if i == 0:
#         root = Node(a[i])
#     else:
#         root.insert(a[i])
# root.search(34)



# --------------------------------- homework -----------------------------------
# 1. Напишите рекурсивную функцию, чтобы сгенерировать и вернуть список от 1 до N.
# Аргументом функции является только N.
# 2. Напишите функцию, которая рекурсивно ищет в сложном объекте значение. Сложный
# объект — это будет список списков списков и т.д. Например, [1, 2, [3, 4, [5, [6, []]]]]. Функция
# должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных
# игнорировать его.



