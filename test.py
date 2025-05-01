import datetime

# Відповідність днів тижня до чисел
days_ua = {
    "понеділок": 0,
    "вівторок": 1,
    "середа": 2,
    "четвер": 3,
    "пʼятниця": 4,
    "субота": 5,
    "неділя": 6
}

# Ввід користувача
day_input = input("Введіть день тижня (українською, з малої літери): ").strip().lower()

if day_input in days_ua:
    today = datetime.date.today()
    today_weekday = today.weekday()
    target_weekday = days_ua[day_input]

    days_ahead = (target_weekday - today_weekday) % 7
    target_date = today + datetime.timedelta(days=days_ahead)

    print(f"{day_input.capitalize()} буде {target_date.strftime('%d.%m.%Y')}")
else:
    print("Неправильний ввід. Спробуйте ще раз.")
