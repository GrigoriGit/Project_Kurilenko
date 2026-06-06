#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Количество положительных элементов в первой половине:
f1 = open('numbers_11.txt', 'w')
f1.write('-15 23 -8 42 -3 17 -11 5 -27 32')
f1.close()
f1 = open('numbers_11.txt', 'r')
content = f1.read()
f1.close()
num_list = content.split()
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
min_element = num_list[0]
for i in range(len(num_list)):
    if num_list[i] < min_element:
        min_element = num_list[i]

half_index = len(num_list) // 2
positive_count = 0
for i in range(half_index):
    if num_list[i] > 0:
        positive_count = positive_count + 1
f2 = open('result_11.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.write(content)
f2.write('\n')
f2.write('Количество элементов: ')
f2.write(str(len(num_list)))
f2.write('\n')
f2.write('Минимальный элемент: ')
f2.write(str(min_element))
f2.write('\n')
f2.write('Количество положительных элементов в первой половине: ')
f2.write(str(positive_count))
f2.close()
