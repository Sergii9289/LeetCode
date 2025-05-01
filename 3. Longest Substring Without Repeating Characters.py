s = "aabaab!bb"
l = list(s)
nl = []
ans = 0

for i in l:
    if i not in nl:
        nl.append(i)
        ans = max(ans, len(nl))  # Використовуємо max() для збереження найкращого результату
    else:
        nl = nl[nl.index(i) + 1:]  # Видаляємо все ДО і включно з повтором
        nl.append(i)  # Додаємо символ після оновлення списку

print(ans)  # Виведе: 3


