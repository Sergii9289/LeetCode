a = '1010'
b = '1011'
a1 = int(a, 2)
b1 = int(b, 2)

num = a1 + b1  # Приклад десяткового числа
binary_num = bin(int(a, 2) + int(b, 2))[2:]  # Видаляємо "0b" на початку
print(binary_num)  # Виведе: "1010"