import datetime

curr_date = datetime.datetime.now().date()
file_name = f'log_function_call_{curr_date}.txt'


def log_line(func_name, error=None):
    return f'Call:{datetime.datetime.now()}.Name:{func_name}.Status:{error if error else "OK"}\n'


def log_call(function):
    def wrapper(*args, **kwargs):
        func_name = function.__name__
        try:
            result = function(*args, **kwargs)
            print(f'Function call: {func_name}. All ok')
            with open(file_name, 'a') as file:
                file.write(log_line(func_name))  # Використання функції log_line
            return result
        except Exception as e:
            with open(file_name, 'a') as file:
                file.write(log_line(func_name, error=e))  # Використання функції log_line
            print(f'Something wrong with {func_name}. Error is: {e}')

    return wrapper


@log_call
def div(a):
    return a / 0


div(2)