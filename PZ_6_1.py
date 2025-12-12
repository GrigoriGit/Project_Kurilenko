#Дан список A размера N (N — четное число). Вывести его элементы с четными
#номерами в порядке возрастания номеров: A2, A4, A6, ..., AN. Условный оператор не
#использовать.
import sys
count = 0
N = 0
A = []
try:
 N = int(input("Введите четное число - "))
except ValueError:
 print("Ошибка, ввы ввели не число")
 sys.exit()
while N % 2 != 0:
 try:
    N = int(input("Введите четное число - "))
 except ValueError:
    print("Ошибка, ввы ввели не число")
    sys.exit()
for i in range(N):
 count += 1
 A.append(count)
for i in range(0, len(A), 2):
 print(A[i])
