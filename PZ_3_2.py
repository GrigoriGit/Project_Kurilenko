# Дано целое число, лежащее в диапазоне 1-999. Вывести его строку- описание вида
# «четное двузначное число», «нечетное трехзначное число» и т. д.
try:
    chislo = int(input("Введите число, лежащее в диапазоне 1-999 -"))
    while chislo < 1 or chislo > 999:
        chislo = int(input("Введите число, лежащее в диапазоне 1-999 -"))
    opisanie = ""
    if chislo % 2 == 0:
        opisanie += "четное"
    else:
        opisanie += " нечетное"
    if chislo >= 1 and chislo < 10:
        opisanie += " однозначное"
    elif chislo >= 10 and chislo < 100:
        opisanie += " двухзначное"
    else:
        opisanie += " трехзначное"
    opisanie += " число"
    print(opisanie)

except ValueError:
    print("Ошибка! Было введено не число")
