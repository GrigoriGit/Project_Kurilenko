#В магазинах имеются следующие товары.
#Магнит – молоко, соль, сахар, печенье, сыр.
#Пятерочка – мясо, молоко, сыр.
# Перекресток – молоко, творог, сыр, сахар, печенье.
# Лента – печенье, молоко, сыр.
#Определить:
#1. в каких магазинах нельзя приобрести соль.
#2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
#3. в каких магазинах можно приобрести мясо и молоко.

magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"печенье", "молоко", "сыр"}
print("в каких магазинах нельзя приобрести соль")
if "соль" not in magnit:
    print("Магнит")
if "соль" not in pyaterochka:
    print("Пятерочка")
if "соль" not in perekrestok:
    print("Перекресток")
if "соль" not in lenta:
    print("Лента")
print("в каких магазинах можно приобрести одновременно молоко, печенье и сыр")
if "молоко" in magnit and "печенье" in magnit and "сыр" in magnit:
    print("Магнит")
if "молоко" in pyaterochka and "печенье" in pyaterochka and "сыр" in pyaterochka:
    print("Пятерочка")
if "молоко" in perekrestok and "печенье" in perekrestok and "сыр" in perekrestok:
    print("Перекресток")
if "молоко" in lenta and "печенье" in lenta and "сыр" in lenta:
    print("Лента")
print("в каких магазинах можно приобрести мясо и молоко")
if "мясо" in magnit and "молоко" in magnit:
    print("Магнит")
if "мясо" in pyaterochka and "молоко" in pyaterochka:
    print("Пятерочка")
if "мясо" in perekrestok and "молоко" in perekrestok:
    print("Перекресток")
if "мясо" in lenta and "молоко" in lenta:
    print("Лента")
