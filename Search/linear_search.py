import random

def linear_search(arr, target):
    # Проходим по всем элементам массива
    for index, value in enumerate(arr):
        if value == target:
            return index  # Возвращаем индекс найденного элемента
    return -1  # Если элемент не найден


if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    target = random.choice(sample_array)  # Выбираем случайный элемент для поиска
    print("Исходный массив:", sample_array)
    print("Элемент для поиска:", target)
    result = linear_search(sample_array, target)
    if result != -1:
        print(f"Элемент найден на индексе: {result}")
    else:
        print("Элемент не найден.")
