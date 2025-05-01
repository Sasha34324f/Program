from tkinter import *
from tkinter import ttk
import datetime

win = Tk()
win.title("Pogoda Program")
win.geometry("600x300")
win.resizable(False, False)  # Заборона зміни розміру вікна
def get_into():
    info1 = ent.get()
    into2 = combo.get()
    info3 = ent2.get()
    days_ua = {
        "Понеділок": 0,
        "Вівторок": 1,
        "Середа": 2,
        "Четвер": 3,
        "Пʼятниця": 4,
        "Субота": 5,
        "Неділя": 6
    }
    day_input = combo.get()
    if day_input in days_ua:
        today = datetime.date.today()
        today_weekday = today.weekday()
        target_weekday = days_ua[day_input]

        days_ahead = (target_weekday - today_weekday) % 7
        target_date = today + datetime.timedelta(days=days_ahead)
        print(target_date)

        nap3.config(text="Дата: " + target_date.strftime('%d.%m.%Y'))  # Оновлення тексту лейбла

    print(into2 + " " + info1 +":"+ info3)
nap = Label(win, font=('Comic Sans MS', 20), text="Оберіть день тижня")
nap.place(relx=0.04, rely=0.1)

nap2 = Label(win, font=('Comic Sans MS', 20), text="Оберіть кількість часу")
nap2.place(relx=0.04, rely=0.3)

ent = Entry(win, font=('Comic Sans MS', 20), width=4)
ent.place(relx=0.1, rely=0.45)

ent2 = Entry(win, font=('Comic Sans MS', 20), width=4)
ent2.place(relx=0.3, rely=0.45)

nap2 = Label(win, font=('Comic Sans MS', 20), text="год")
nap2.place(relx=0.22, rely=0.45)

nap2 = Label(win, font=('Comic Sans MS', 20), text="хв")
nap2.place(relx=0.44, rely=0.45)

but = Button(win, text="Провести заміри", font=('Comic Sans MS', 20), width=13, height=1, command=get_into)
but.place(relx=0.07, rely=0.65)

#result
nap3 = Label(win, font=('Comic Sans MS', 20), text="Дата: ")
nap3.place(relx=0.6, rely=0.1)

options = ["Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця", "Субота", "Неділя"]
# Створюємо Combobox
combo = ttk.Combobox(win, values=options, font=('Comic Sans MS', 14), width=15)
combo.set("Оберіть варіант")  # Початковий текст
combo.place(relx=0.1, rely=0.22)

# Функція при виборі
def on_select(event):
    q = combo.get()
    print(f"Ви вибрали: {q}")

# Прив'язуємо подію вибору
combo.bind("<<ComboboxSelected>>", on_select)

win.mainloop()
