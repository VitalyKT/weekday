import datetime

def weekdayInput(year, month, day):
    date = datetime.date(year, month, day)
    return date.weekday()

# Использование функции
day = int(input('Введите день\n'))
month = int(input('Введите месяц\n'))
year = int(input('Введите год\n'))

weekday_number = weekdayInput(year, month, day)

# Вывод дня недели
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"]
print(f"{year}-{month}-{day} это {weekdays[weekday_number]}")