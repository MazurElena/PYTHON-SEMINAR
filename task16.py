# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь 
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

n = int(input("введите колличество элементов в списке: "))
my_list = []
# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(i+1)
# заполнили список значениями
GenNewList(n,my_list)

print(*my_list)
x = int(input("введите число X для поиска: "))
# вывели результат
print(f"{my_list.count(x)} раз встречается")