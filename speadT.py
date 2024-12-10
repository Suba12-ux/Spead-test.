"""Сравниваем множества, списки и кортежи"""
from time import time
from sys import getsizeof

# Просьба не ставить большие числа. В count хранится правая граница range для объектов.
# В foriner – правая граница for ... in range

count = 10000000
foriner = count

print("В этом алгоритме сравниваются множество, список и кортеж на скорость и время", end="\n\n")
print("Правая граница интервала —", count)
my_set = set(range(1, count + 1))
my_list = list(range(1, count + 1))
my_tuple = tuple(range(1, count + 1))

my_set_size = getsizeof(my_set)
my_list_size = getsizeof(my_list)
my_tuple_size = getsizeof(my_tuple)

print()
print(f"Память {{множес.}} = {my_set_size} байт = {round(my_set_size / 1024, 3)} Кб \
    = {round(my_set_size / 1024 / 1024, 3)} Мб")
print(f"Память [списка]  = {my_list_size} байт = {round(my_list_size / 1024, 3)} Кб \
    = {round(my_list_size / 1024 / 1024, 3)} Мб")
print(f"Память (кортежа) = {my_tuple_size} байт = {round(my_tuple_size / 1024, 3)} Кб \
    = {round(my_tuple_size / 1024 / 1024, 3)} Мб")

print()

t = time()
for i in range(foriner):
    if i in my_set:
        pass
print(f"Время с множеством: {time() - t} секунд")
my_set.clear()

t = time()
for i in range(foriner):
    if i in my_list:
        pass
print(f"Время с списком:    {time() - t} секунд")
my_list.clear()

t = time()
for i in range(foriner):
    if i in my_tuple:
        pass
print(f"Время с кортежом:   {time() - t} секунд")