nums = [1,3,5,6]
target = 7

def binary_search(array, target):
    left, right = 0, len(array) - 1
    if max(array) < target:
        return len(array)

    while left <= right:
        mid = (left + right) // 2  # Знаходимо середній індекс

        if array[mid] == target:
            return mid  # Елемент знайдено, повертаємо індекс

        elif array[mid] < target:
            left = mid + 1  # Шукаємо в правій половині

        else:
            right = mid - 1  # Шукаємо в лівій половині

    return left # Елемент не знайдено
print(binary_search(nums, target))