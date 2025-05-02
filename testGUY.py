from tkinter import *
from tkinter import ttk
import datetime

win = Tk()
win.title("Pogoda Program")
win.geometry("600x300")
win.resizable(False, False)
win.configure(bg='#f0f8ff')  # світлий фон

def get_into():
    info1 = ent.get()
    into2 = combo.get()
    info3 = ent2.get()
    days_ua = {
        "Понеділок": 0,
        "Вівторок": 1,
        "Середа": 2,
        "Четвер": 3,
        "П'ятниця": 4,
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
        nap3.config(text="Дата: " + target_date.strftime('%d.%m.%Y'))

    print(into2 + " " + info1 + ":" + info3)

# Заголовки
nap = Label(win, font=('Comic Sans MS', 18), text="Оберіть день тижня", bg='#f0f8ff')
nap.place(relx=0.04, rely=0.1)

nap2 = Label(win, font=('Comic Sans MS', 18), text="Оберіть кількість часу", bg='#f0f8ff')
nap2.place(relx=0.04, rely=0.3)

# Entry для годин і хвилин
ent = Entry(win, font=('Comic Sans MS', 18), width=4)
ent.place(relx=0.1, rely=0.45)

ent2 = Entry(win, font=('Comic Sans MS', 18), width=4)
ent2.place(relx=0.3, rely=0.45)

Label(win, font=('Comic Sans MS', 18), text="год", bg='#f0f8ff').place(relx=0.2, rely=0.45)
Label(win, font=('Comic Sans MS', 18), text="хв", bg='#f0f8ff').place(relx=0.42, rely=0.45)

# Кнопка
but = Button(win, text="Провести заміри", font=('Comic Sans MS', 18), width=16, height=1, command=get_into, bg='#add8e6')
but.place(relx=0.07, rely=0.65)

# Label для виводу дати (праворуч!)
nap3 = Label(win, font=('Comic Sans MS', 18), text="Дата: ", bg='#f0f8ff')
nap3.place(relx=0.65, rely=0.1)

# Combobox
options = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
combo = ttk.Combobox(win, values=options, font=('Comic Sans MS', 14), width=15)
combo.set("Оберіть варіант")
combo.place(relx=0.1, rely=0.22)

def on_select(event):
    q = combo.get()
    print(f"Ви вибрали: {q}")

combo.bind("<<ComboboxSelected>>", on_select)

win.mainloop()
