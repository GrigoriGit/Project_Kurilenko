#В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(*row)
N = int(input(f"Введите номер строки N (от 0 до {rows - 1}): "))
if 0 <= N < rows:
    target_row = matrix[N]    
    row_sum = sum(target_row)   
    row_product = 1
    for num in target_row:
        row_product *= num
    print("Сумма элементов строки", N, ":", row_sum)
    print("Произведение элементов строки", N, ":", row_product)
else:
    print("Строки с таким номером не существует")
