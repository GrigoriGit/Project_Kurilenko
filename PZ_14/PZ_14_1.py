#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать егo
#в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).
from tkinter import *
root = Tk()
root.title("Contact Us")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg="#bfbfbf")
header = Label(
root,
text="Contact Us",
bg="#4d4d4d",
fg="black",
font=("Arial", 24, "bold"),
width=25,
height=2
)
header.grid(row=0, column=0, pady=(20, 30))
Label(
root,
text="First Name",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=1, column=0, sticky=W, padx=60)
entry_first = Entry(root, width=35)
entry_first.grid(row=2, column=0, padx=60, pady=5)
Label(
root,
text="Last Name",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=3, column=0, sticky=W, padx=60)
entry_last = Entry(root, width=35)
entry_last.insert(0, "*Smith*")
entry_last.grid(row=4, column=0, padx=60, pady=5)
Label(
root,
text="Email",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=5, column=0, sticky=W, padx=60)
entry_email = Entry(root, width=35)
entry_email.insert(0, "Email address")
entry_email.grid(row=6, column=0, padx=60, pady=5)
Label(
root,
text="Website",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=7, column=0, sticky=W, padx=60)
entry_website = Entry(root, width=35)
entry_website.insert(0, "www.example.com")
entry_website.grid(row=8, column=0, padx=60, pady=5)
Label(
root,
text="Password",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=9, column=0, sticky=W, padx=60)
entry_password = Entry(root, width=35)
entry_password.insert(0, "8-10 characters")
entry_password.grid(row=10, column=0, padx=60, pady=5)
Label(
root,
text="Password Confirmation",
bg="#bfbfbf",
font=("Arial", 12)
).grid(row=11, column=0, sticky=W, padx=60)
entry_confirm = Entry(root, width=35)
entry_confirm.insert(0, "Type your password again")
entry_confirm.grid(row=12, column=0, padx=60, pady=5)
button = Button(root, text="Sign Up")
button.grid(row=13, column=0, sticky=W, padx=60, pady=15)
root.mainloop()
