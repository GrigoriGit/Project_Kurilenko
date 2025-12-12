#Составить функцию, которая напечатает сорок любых символов
import random
letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
other = "!@#$%^&*()_+=-/?.>,<`~"
simvoli = letters + letters.upper() + numbers + other
def funkcia():
    result = ""
    for i in range(40):
        result += random.choice(simvoli)
    return result
print(funkcia())