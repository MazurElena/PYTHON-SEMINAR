# Задача 4:Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Input: 6 
# Output: 1 4 1
# Input: 24 
# Output: 4 16 4
# Input: 60 
# Output: 10 40 10

count = int(input("Введите количество сделаных журавликов: "))

print(f"Петя сделал:\t{int(count/6)} журавликов;" + 
      f"\nКатя сделала:\t{int(count*2/3)} журавликов;" + 
      f"\nСережа сделал:\t{int(count/6)} журавликов;")