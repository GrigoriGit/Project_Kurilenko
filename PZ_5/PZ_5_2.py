#Описать функцию SortInc3(A, B, C), меняющую содержимое переменных A, B, C
#таким образом, чтобы их значения оказались упорядоченными по возрастанию (A,
#B, C — вещественные параметры, являющиеся одновременно входными и
#выходными). С помощью этой функции упорядочить по возрастанию два данных
#набора из трех чисел: (Ai, Bi, Ci) и (A2, B2, C2).
import sys
def SortInc3(A, B, C):
    spisok = [A, B, C]
    sorted_spisok = sorted(spisok)
    A = sorted_spisok[0]
    B = sorted_spisok[1]
    C = sorted_spisok[2]
    return A, B, C
try:
    Ai = input("Введите вещественное число Ai - ")
    Bi = input("Введите вещественное число Bi - ")
    Ci = input("Введите вещественное число Ci - ")
    A2 = input("Введите вещественное число A2 - ")
    B2 = input("Введите вещественное число B2 - ")
    C2 = input("Введите вещественное число C2 - ")
    Ai = float(Ai)
    Bi = float(Bi)
    Ci = float(Ci)
    A2 = float(A2)
    B2 = float(B2)
    C2 = float(C2)
except ValueError:
    print("Ошибка, вы ввели не число")
    sys.exit()
Ai, Bi, Ci = SortInc3(Ai, Bi, Ci)
print("Ai, Bi, Ci =", Ai, ",", Bi, ",", Ci)
A2, B2, C2 = SortInc3(A2, B2, C2)
print("A2, B2, C2 =", A2, ",", B2, ",", C2)
