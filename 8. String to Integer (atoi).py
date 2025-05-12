def extract_first_int(s):
    import re
    # Видаляємо початкові пробіли
    s = s.lstrip()

    # Якщо рядок починається не з цифри або знака `+/-`, повертаємо 0
    if not re.match(r"^[+-]?\d", s):
        return 0

    # Шукаємо перше число зі знаком
    match = re.search(r"^[+-]?\d+", s)

    if match:
        num = int(match.group())  # Перетворюємо у число

        # Обмежуємо значення в межах 32-бітного int
        num = max(min(num, 2 ** 31 - 1), -2 ** 31)
        return num

    return 0


# Тестові випадки
print(extract_first_int(".1"))  # Виведе: 0
print(extract_first_int("42"))  # Виведе: 42
print(extract_first_int("    -42"))  # Виведе: -42
print(extract_first_int("text 56"))  # Виведе: 0
print(extract_first_int("-91283472332"))  # Виведе: -2147483648