def merge(nums1, m, nums2, n):
    # Індекси для проходу по nums1 і nums2
    i, j, k = m - 1, n - 1, m + n - 1

    # Заповнюємо nums1 з кінця
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]  # Переміщаємо nums1[i] на останню позицію
            i -= 1
        else:
            nums1[k] = nums2[j]  # Переміщаємо nums2[j]
            j -= 1
        k -= 1  # Зменшуємо позицію для заповнення

# Приклад
nums1 = [1, 2, 3, 0, 0, 0]  # `0` означає місце для nums2
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Виведе: [1, 2, 2, 3, 5, 6]