# Ієрархія користувацьких виключень

# Створіть базовий клас виключень ApplicationError і два підкласи NegativeValueError та ValueTooLargeError.
# Реалізуйте функцію check_number, яка буде викликати відповідне виключення, якщо число від'ємне або занадто велике.
# Обробіть виключення в блоці try-except.

# Напишіть тут ваш код
class ApplicationError(Exception):
    pass


class NegativeValueError(ApplicationError):
    def __init__(self, value, message='Значення не повинно бути менше нуля'):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'


class ValueTooLargeError(ApplicationError):
    def __init__(self, value, message='Значення занадто велике'):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'

def check_number(num):
    if num < 0:
        raise NegativeValueError(num)
    elif num > 100:
        raise ValueTooLargeError(num)

try:
    check_number(int(input('Введіть число: ')))
except (NegativeValueError, ValueTooLargeError) as e:
    print(f'Сталась помилка: {e}')
except ApplicationError as e:
    print(f'Сталась загальна помилка: {e}')
except Exception as e:
    print(f'Захоплення всіх помилок: {e}')
else: print('Все гаразд')