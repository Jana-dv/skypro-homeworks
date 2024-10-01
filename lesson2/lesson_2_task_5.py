def month_to_season(number):
    if number > 2 and number < 6:
        return "Весна"
    if number > 5 and number < 9:
        return "Лето"
    if number > 8 and number < 12:
        return "Осень"
    if number > 0 and number < 13:
        return "Зима"

print(month_to_season(7))    