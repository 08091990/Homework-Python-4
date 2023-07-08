#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

import random
N = int(input("Введите количество элементов первого множества: "))
array_1 = [] 
for i in range(N):
    array_1.append(random.randint(1, N)) 
print(array_1) 
M = int(input("Введите количество элементов второго множества: "))
array_2 = [] 
for i in range(N):
    array_2.append(random.randint(1, N)) 
print(array_2) 
my_set_1 = set(array_1)
my_set_2 = set(array_2)
i = my_set_1.intersection(my_set_2)
print(i)



#index = 0
#nearest_value = array[0] 
#min_difference = abs(array[i] - b)
#for i in range(N):
    #difference = abs(array[i] - b)
    #if difference < min_difference:
        #min_difference = difference
        #nearest_value = array[i]
        #index = i
#print(f"Ближайшее значение: {nearest_value}")