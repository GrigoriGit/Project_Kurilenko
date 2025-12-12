#Дано число R и список A размера N. Найти элемент списка, который наиболее
#близок к числу R (то есть такой элемент AK, для которого величина |AK - R| является
#минимальной).
import random
import sys
try:
    N = int(input("Введите размеры списка - "))
    R = int(input("Введите число R - "))
except ValueError:
    print("Ошибка, вы ввели не число")
    sys.exit()
A = []
smallest = None
for i in range(N+1):
    A.append(random.randint(0,1000))
for i in A:
    if smallest == None:
        smallest = i
    raznica = i - R
    if raznica < 0:
        raznica *= -1
    if raznica < smallest:
        smallest = i
print(A)
print("Элемент списка, который наиболее близок к числу R -", smallest)
