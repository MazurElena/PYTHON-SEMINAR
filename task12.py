# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
from datetime import datetime
s = int(input("введите число S сумма чисел "))
p = int(input("введите число P произведение чисел "))
start_time = datetime.now()
for i in range(s):
    for j in range(p):
        if s == i+j and p == i*j:
            print(f"{s}={i+j} {p}={i*j}")
            print(f"Возможно это числа {i}, {j}")
print(datetime.now() - start_time)