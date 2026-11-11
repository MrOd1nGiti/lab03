charge = int(input("Введите заряд аккумулятора (от 0 до 100): "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif 0 <= charge <= 19:
    print("Низкий")
elif 20 <= charge <= 79:
    print("Средний")
else:
    print("Высокий")

year = int(input("Введите год для проверки на високосный (от 1 до 9999): "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Год {year}: да, високосный")
else:
    print(f"Год {year}: нет, не високосный")
