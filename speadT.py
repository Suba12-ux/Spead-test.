class Spd:
	@staticmethod
	def met1():
		#*********************************************** Функция для вычисления чисел Фибоначчи без кэширования ***********************************************
		from functools import lru_cache
		import time
		def fib_none_cache(n):
		    txt = [1, 1]
		    [txt.append(txt[-1]+txt[-2]) for i in range(n)]
		    return txt

		# Начало времени выполнения
		begin = time.time()
		x = fib_none_cache(30)
		x2 = fib_none_cache(30)
		x3 = fib_none_cache(30)
		# Конец времени выполнения
		end = time.time()
		print(f"Время, затраченное на выполнение функции без lru_cache: {str(end-begin)[0:4]} сек.", str(x)[:-15], sep='\n')

		#*********************************************** Функция для вычисления чисел Фибоначчи с кэшированием ***********************************************

		@lru_cache (maxsize=100) 
		def fib_without_cache(n):
		    txt = [1, 1]
		    [txt.append(txt[-1]+txt[-2]) for i in range(n)]
		    return txt

		begin = time.time()
		x = fib_without_cache(30)
		x2 = fib_without_cache(30)
		x3 = fib_without_cache(30)
		end = time.time()
		print(f"Время, затраченное на выполнение функции с lru_cache: {str(end-begin)[0:4]} сек.", str(x)[:-15], sep='\n')

		print('Это объясняется тем, что за счёт кэширования повторные вызовы функции с одинаковыми аргументами выполняются быстрее, так как результат берётся из кэша, а не вычисляется заново. \nНо показатели будут варьиорваться в зависимости от используемого типа данных и частоты процессора.')

		#*********************************************** Доп Инфа ***********************************************


	@staticmethod
	def met2():
		"""Сравниваем множества, списки и кортежи"""
		from time import time
		from sys import getsizeof

		# Просьба не ставить большие числа. В count хранится правая граница range для объектов.
		# В foriner – правая граница for ... in range

		count = 10000
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

		

from tkinter import *
window  = Tk()
window.title("Tested")
window.geometry("300x100")

def go1():
	print(Spd.met1())
	print('****************************************************************')

def go2():
	print(Spd.met2())
	print('****************************************************************')

menu_bar = Menu(window)
window.config(menu = menu_bar)
text1 = Label(window, text = 'К запуску готов!')
text1.pack()
button1 = Button(window, text = "1", command = go1)
button1.pack()
button2 = Button(window, text = "2", command = go2)
button2.pack()
menu_bar.add_command(label = "Quit", command = window.quit)

window.mainloop()
