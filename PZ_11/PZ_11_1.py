
#В последовательности на n целых чисел найти и вывести:
#минимальный среди положительных
#элементы кратные пяти
#их среднее арифметическое
import random
n = int(input("Введите количество элементов: "))
A = [random.randint(-100, 100) for i in range(n)]
print("Исходная последовательность:", A)
positive_numbers = [i for i in A if i > 0]
if positive_numbers:
    min_positive = min(positive_numbers)
    print("Минимальный среди положительных:", min_positive)
else:
    print("Положительных элементов нет")

multiples_of_five = [i for i in A if i % 5 == 0]
print("Элементы кратные пяти:", multiples_of_five)

if multiples_of_five:
    average = sum(multiples_of_five) / len(multiples_of_five)
    print("Среднее арифметическое элементов кратных пяти:", average)
else:
    print("Элементов кратных пяти нет")
