#Разработать программу с применением пакета tk, взяв в качестве 
#условия одну любую задачу из ПЗ №№ 1-9.
from tkinter import *
root = Tk()
root.title("Магазины")
root.geometry("700x400")
magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"печенье", "молоко", "сыр"}
def solve():
result.delete("1.0", END)
result.insert(END, "В каких магазинах нельзя приобрести соль:\n")
if "соль" not in magnit:
    result.insert(END, "Магнит\n")
if "соль" not in pyaterochka:
    result.insert(END, "Пятерочка\n")
if "соль" not in perekrestok:
    result.insert(END, "Перекресток\n")
if "соль" not in lenta:
    result.insert(END, "Лента\n")
result.insert(END, "\n")
result.insert(
    END,
    "В каких магазинах можно приобрести одновременно молоко, печенье и сыр:\n"
)
if "молоко" in magnit and "печенье" in magnit and "сыр" in magnit:
    result.insert(END, "Магнит\n")
if (
    "молоко" in pyaterochka
    and "печенье" in pyaterochka
    and "сыр" in pyaterochka
):
    result.insert(END, "Пятерочка\n")
if (
    "молоко" in perekrestok
    and "печенье" in perekrestok
    and "сыр" in perekrestok
):
    result.insert(END, "Перекресток\n")
if "молоко" in lenta and "печенье" in lenta and "сыр" in lenta:
    result.insert(END, "Лента\n")
result.insert(END, "\n")
result.insert(
    END,
    "В каких магазинах можно приобрести мясо и молоко:\n"
)
if "мясо" in magnit and "молоко" in magnit:
    result.insert(END, "Магнит\n")
if "мясо" in pyaterochka and "молоко" in pyaterochka:
    result.insert(END, "Пятерочка\n")
if "мясо" in perekrestok and "молоко" in perekrestok:
    result.insert(END, "Перекресток\n")
if "мясо" in lenta and "молоко" in lenta:
    result.insert(END, "Лента\n")
label = Label(
root,
text="Задача о магазинах",
font=("Arial", 14)
)
label.pack(pady=10)
button = Button(
root,
text="Выполнить",
command=solve
)
button.pack(pady=10)
result = Text(root, width=70, height=15)
result.pack(padx=10, pady=10)
root.mainloop()
