#Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год
#и поместить ее в новый текстовый файл.
import re
with open('Dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()
pattern = r'1857\s*год[^1-9]*'
match = re.search(pattern, text, re.DOTALL)
if match:
    block_1857 = match.group(0)
else:
    block_1857 = ""
with open('block_1857.txt', 'w', encoding='utf-8') as f:
    f.write(block_1857)
print("Блок информации за 1857 год сохранен в файл block_1857.txt")
