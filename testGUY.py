from g4f.client import Client
from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

win = Tk()
win.title("Pogoda Program")
win.geometry("600x300")
win.resizable(False, False)
win.configure(bg='#f0f8ff')

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

    days_ua_url = {
        0: "ponedilok",
        1: "vivtorok",
        2: "sereda",
        3: "chetver",
        4: "pyatnytsya",
        5: "subota",
        6: "nedilya"
    }

    day_input = combo.get()
    if day_input in days_ua:
        today = datetime.today()
        today_weekday = today.weekday()
        target_weekday = days_ua[day_input]
        days_ahead = (target_weekday - today_weekday) % 7
        target_date = today + timedelta(days=days_ahead)
        nap3.config(text="Дата: " + target_date.strftime('%d.%m.%Y'))
    else:
        print("Невірний день тижня")
        return

    user_date = target_date.strftime('%d.%m.%Y')

    def get_sinoptik_weather_by_date(input_date_str):
        try:
            date = datetime.strptime(input_date_str, "%d.%m.%Y")
            weekday_number = date.weekday()
            formatted_date = date.strftime("%Y-%m-%d")

            if date.date() == datetime.now().date():
                url = "https://sinoptik.ua/pohoda/chernihiv"
            else:
                day_part = days_ua_url.get(weekday_number, "")
                url = f"https://sinoptik.ua/pohoda/chernihiv/{day_part}"

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except ValueError:
            print("❌ Неправильний формат дати")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Помилка при з'єднанні: {e}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        general_forecast = soup.select_one("p.GVzzzKDV")
        if general_forecast:
            nap5.config(text=general_forecast.text.strip())
        else:
            nap5.config(text="⚠️ Не вдалося знайти загальний прогноз.")
            return None

        hours = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        temp_blocks = [el.text.strip() for el in soup.select("td.lgo8NaQM") if "°" in el.text.strip()]
        temp_blocks = temp_blocks[:8]
        weather_icons = soup.select("td.lgo8NaQM div[aria-label]")
        weather_conditions = [icon['aria-label'].strip() for icon in weather_icons[:8]]

        if len(temp_blocks) == 8 and len(weather_conditions) == 8:
            # Повертаємо перші дані
            return hours[4], temp_blocks[4], weather_conditions[4], general_forecast.text.strip()
        else:
            print("⚠️ Не вдалося зчитати всі погодні дані.")
            return None

    result = get_sinoptik_weather_by_date(user_date)
    if result:
        a, b, c, d = result
        
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Привіт, уяви що ти частина програми для визначення часу для прогулянки. "
                               f"Тобі видають такі дані: час — {a}, температура — {b}, погода — {c}. "
                               f"Загальний прогноз — {d}. Час прогулянки —  {info1}години {info3} хвилини. "
                               f"Вирахуй найкращий час для прогулянки на свіжому повітрі з урахуванням світанку, заходу сонця, тощо, якщо цілий день дощ то скажи що краще сьогодні не йти на прогулянку "
                               f"Напиши результат у форматі: 'За моїми підрахунками найкращий час для прогулянки — з ... до ...' і більше ніяких пояснень тільки за форматом"
                }
            ]
        )
        print(response.choices[0].message.content)
        nap6.config(text=response.choices[0].message.content)

        but = Button(win, text="⮕", font=('Comic Sans MS', 10), width=3, height=1, command=gpt, bg='#add8e6')
        but.place(relx=0.94, rely=0.88)
def gpt():
    
    
    win = Tk()
    win.title("Виписка погоди")
    
    win.mainloop()


        
       
        

# GUI
nap = Label(win, font=('Comic Sans MS', 18), text="Оберіть день тижня", bg='#f0f8ff')
nap.place(relx=0.04, rely=0.1)

nap2 = Label(win, font=('Comic Sans MS', 18), text="Оберіть кількість часу", bg='#f0f8ff')
nap2.place(relx=0.04, rely=0.3)

ent = Entry(win, font=('Comic Sans MS', 18), width=4)
ent.place(relx=0.1, rely=0.45)

ent2 = Entry(win, font=('Comic Sans MS', 18), width=4)
ent2.place(relx=0.3, rely=0.45)

Label(win, font=('Comic Sans MS', 18), text="год", bg='#f0f8ff').place(relx=0.2, rely=0.45)
Label(win, font=('Comic Sans MS', 18), text="хв", bg='#f0f8ff').place(relx=0.42, rely=0.45)

but = Button(win, text="Провести заміри", font=('Comic Sans MS', 18), width=16, height=1, command=get_into, bg='#add8e6')
but.place(relx=0.07, rely=0.65)

nap3 = Label(win, font=('Comic Sans MS', 18), text="Дата: ", bg='#f0f8ff')
nap3.place(relx=0.55, rely=0.1)

nap4 = Label(win, font=('Comic Sans MS', 18), text="📝 Загальний прогноз:", bg='#f0f8ff')
nap4.place(relx=0.45, rely=0.2)
nap4 = Label(win, font=('Comic Sans MS', 18), text="Прогноз прогулянки:", bg='#f0f8ff')
nap4.place(relx=0.53, rely=0.6)


nap5 = Message(win, font=('Comic Sans MS', 10), text="", bg='#f0f8ff', width=250)
nap5.place(relx=0.5, rely=0.3)

nap6 = Message(win, font=('Comic Sans MS', 10), text="", bg='#f0f8ff', width=250)
nap6.place(relx=0.53, rely=0.7)

options = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
combo = ttk.Combobox(win, values=options, font=('Comic Sans MS', 14), width=15)
combo.set("Оберіть варіант")
combo.place(relx=0.1, rely=0.22)

def on_select(event):
    q = combo.get()
    print(f"Ви вибрали: {q}")

combo.bind("<<ComboboxSelected>>", on_select)

win.mainloop()
