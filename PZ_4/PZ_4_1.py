# Дано целое число N (>0).
# Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
try:
  N = int(input("Введите число, которое больше нуля - "))
  while N <= 0:
    N = int(input("Введите число, которое больше нуля -"))
  proizvedenie = 1
  for i in range(N + 1):
    a  = 1 + i / 10 ** (len(str(i)))
    proizvedenie *= a
  print(proizvedenie)
except:
  print("Ошибка! Вы ввели не число!")
