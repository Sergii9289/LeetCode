digits = [4, 3, 9, 9]
# st_num = ''.join(map(str, digits))  # Перетворюємо числа в строки
# num = int(st_num) + 1
new_digits = list(map(int, str(int(''.join(map(str, digits))) + 1)))
print(new_digits)