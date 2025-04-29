import traceback

def complex_operation(data):
    def step_one(data):
        # Викликає TypeError, якщо не список
        if not isinstance(data, list):
            raise TypeError("Очікував список!")
        return [x ** 2 for x in data]

    def step_two(processed_data):
        # Викидає ValueError, якщо список порожній
        if len(processed_data) == 0:
            raise ValueError("Список порожній!")
        return sum(processed_data)

    def step_three(result):
        # Викидає ArithmeticError, якщо результат від'ємний
        if result < 0:
            raise ArithmeticError("Результат не може бути від'ємним!")
        return f"Результат: {result}"

    try:
        # Послідовний виклик функцій
        processed_data = step_one(data)
        result = step_two(processed_data)
        return step_three(result)
    except Exception as e:
        # Витягнення трасування стека
        tb = traceback.extract_tb(e.__traceback__)
        print("Сталася помилка! Трасування стека:")
        for frame in tb:
            print(f"Файл: {frame.filename}")
            print(f"Рядок: {frame.lineno}")
            print(f"Ім'я функції: {frame.name}")
            print(f"Текст рядка: {frame.line}")
            print("-" * 50)

# Приклад використання:
# Викличе TypeError
complex_operation("не список")

# Викличе ValueError
complex_operation([])

# Успішний випадок
print(complex_operation([1, 2, 3]))