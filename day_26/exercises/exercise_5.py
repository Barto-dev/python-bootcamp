weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


weather_f = {day: to_fahrenheit(temp_c) for (day, temp_c) in weather_c.items()}
print(weather_f)
