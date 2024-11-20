import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Находим середину
        if arr[mid] == target:
            return mid  # Возвращаем индекс найденного элемента
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине
    return -1  # Если элемент не найден

# Пример использования
if __name__ == "__main__":
    sample_array = sorted([random.randint(1, 100) for _ in range(10)])
    target = random.choice(sample_array)  # Выбираем случайный элемент для поиска
    print("Исходный массив:", sample_array)
    print("Элемент для поиска:", target)
    result = binary_search(sample_array, target)
    if result != -1:
        print(f"Элемент найден на индексе: {result}")
    else:
        print("Элемент не найден.")
