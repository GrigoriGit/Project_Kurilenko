#В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)
print("Исходная матрица:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()
N = int(input("Введите номер строки N (от 0 до " + str(rows-1) + "): "))
if 0 <= N < rows:
    row_sum = 0
    for j in range(cols):
        row_sum = row_sum + matrix[N][j]
    row_product = 1
    for j in range(cols):
        row_product = row_product * matrix[N][j]
    print("Сумма элементов строки", N, ":", row_sum)
    print("Произведение элементов строки", N, ":", row_product)
else:
    print("Строки с таким номером не существует")
