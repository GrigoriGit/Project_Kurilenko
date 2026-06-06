#В матрице найти сумму элементов второй половины матрицы.

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
total_elements = rows * cols
half_count = total_elements // 2
flat_list = []
for i in range(rows):
    for j in range(cols):
        flat_list.append(matrix[i][j])
second_half_sum = 0
for i in range(half_count, total_elements):
    second_half_sum = second_half_sum + flat_list[i]

print("Сумма элементов второй половины матрицы:", second_half_sum)
