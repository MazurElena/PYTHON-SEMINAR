# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений  
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит 
# сами элементы множеств.
import random;
list1 = [] 
list2 = []

ml1 = int(input("введите колличество элементов в первом списке: "))
ml2 = int(input("введите колличество элементов во втором списке: "))

# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(random.randint(1,25))
GenNewList(ml1,list1)
GenNewList(ml2,list2)

print(list1)
print(list2)
 
res_v1 = list(set(list1) & set(list2))
res_v1.sort()
print(f"Первый способ решения {res_v1}")
res_v2= [element for element in set(list1) if element in set(list2)]
res_v2.sort()
print(f"Второй способ решения {res_v2}")