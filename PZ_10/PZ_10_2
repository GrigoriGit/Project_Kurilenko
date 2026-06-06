# Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое, количество знаков препинания.
#Сформировать новый файл, в который поместить строку наименьшей длины.

f = open('text18-11.txt', 'r')
lines = []
for line in f:
    lines.append(line)
f.close()
print("Содержимое файла text18-11.txt:")
for line in lines:
    print(line, end='')
punctuation = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char == '.' or char == ',' or char == '!' or char == '?' or char == ':' or char == ';' or char == '-' or char == '(' or char == ')' or char == '"' or char == "'":
            punctuation = punctuation + 1
print("Количество знаков препинания:", punctuation)
min_len = len(lines[0])
min_line = lines[0]
for i in range(len(lines)):
    if len(lines[i]) < min_len:
        min_len = len(lines[i])
        min_line = lines[i]
f_new = open('shortest_line.txt', 'w')
f_new.write(min_line)
f_new.close()
