from random import randint

print("Массив:")
ar = []
for i in range(10):
    ar.append(randint(-10, 10))
print(ar)

print("\n1 Задание.\nПары отрицательных чисел, стоящих рядом: ")
for i in range(1, len(ar)):
    if ar[i-1]<0 and ar[i]<0:
        print(ar[i-1], ar[i])

print("\n2 Задание\nНовый массив без одинаковых элементов:")
ar2 = set(ar)

print(ar2)
# Вариант 5
# 1. Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных
# чисел, стоящих рядом.
# 2. Дан целочисленный массив размера 10. Создать новый массив, удалив все
# одинаковые элементы, оставив их 1 раз.