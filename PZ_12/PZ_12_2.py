#В матрице найти сумму элементов второй половины матрицы.

rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(*row)
flat_list = [element for row in matrix for element in row]
half_count = (rows * cols) // 2
second_half_sum = sum(flat_list[half_count:])
print("Сумма элементов второй половины матрицы:", second_half_sum)
