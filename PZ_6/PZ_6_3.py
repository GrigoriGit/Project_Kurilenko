#Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
#(при этом AN перейдет в AN-1, AN-1 — в AN-2, .., A2 — в A1, a исходное значение
#первого элемента будет потеряно). Последний элемент полученного списка
#положить равным 0.
import sys
try:
    N = int(input("Введите размеры списка - "))
except ValueError:
    print("Ошибка, вы ввели не число")
    sys.exit()
znachenie = 0
A = []
for i in range(N):
 znachenie += 1
 A.append(znachenie)
print(A)
for i in range(N-1):
    A[i] = A[i+1]
A[N-1] = 0
print(A)
