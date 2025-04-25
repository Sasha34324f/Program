from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Pogoda Program")
win.geometry("500x300")
win.resizable(False, False)  # Заборона зміни розміру вікна
def get_into():
    info1 = ent.get()
    into2 = combo.get()
    nap.config(text=into2+info1)
    print(into2)
nap = Label(win, font=('Comic Sans MS', 20), text="текст для напису")
nap.place(relx=0.1, rely=0.1)

ent = Entry(win, font=('Comic Sans MS', 20), width=10)
ent.place(relx=0.1, rely=0.2)

but = Button(win, text="Click", font=('Comic Sans MS', 20), width=7, height=1, command=get_into)
but.place(relx=0.1, rely=0.35)

options = ["Варіант 1", "Варіант 2", "Варіант 3"]
# Створюємо Combobox
combo = ttk.Combobox(win, values=options, font=('Comic Sans MS', 14), width=15)
combo.set("Оберіть варіант")  # Початковий текст
combo.place(relx=0.1, rely=0.55)

# Функція при виборі
def on_select(event):
    q = combo.get()
    print(f"Ви вибрали: {q}")

# Прив'язуємо подію вибору
combo.bind("<<ComboboxSelected>>", on_select)

win.mainloop()
