class InputValidationError(Exception):
    pass

def validate_input(string):
    try:
        if string == '':
            raise ValueError('Input cannot be empty')
        if len(string) > 10:
            raise ValueError('Input is too long')
    except ValueError as e:
        raise InputValidationError(f'Сталась помилка: {e}') from e

try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")