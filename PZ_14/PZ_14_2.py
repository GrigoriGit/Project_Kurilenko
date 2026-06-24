#Разработать программу с применением пакета tk, взяв в качестве 
#условия одну любую задачу из ПЗ №№ 1-9.
from tkinter import *
root = Tk()
root.title("Задача о двузначном числе")
root.geometry("700x400")
def solve():
    global result, entry
    result.delete("1.0", END)
    try:
        chislo = int(entry.get())
        if chislo < 10 or chislo >= 100:
            result.insert(END, "ошибка\n")
        else:
            result.insert(END, f"Левая цифра  - {chislo // 10}\n")
            result.insert(END, f"Правая цифра  - {chislo % 10}\n")
    except ValueError:
        result.insert(END, "ошибка\n")
label = Label(root, text="Введите двухзначное число:")
label.pack(pady=10)
entry = Entry(root, width=15)
entry.pack(pady=5)
button = Button(root, text="Выполнить", command=solve)
button.pack(pady=10)
result = Text(root, width=70, height=15)
result.pack(padx=10, pady=10)
root.mainloop()
