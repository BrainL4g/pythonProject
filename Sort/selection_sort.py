import random


def selection_sort(arr):
    # Проходим по всем элементам массива
    for i in range(len(arr)):
        # Находим минимальный элемент в оставшейся части массива
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами найденный минимальный элемент с первым элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    print("Исходный массив:", sample_array)
    sorted_array = selection_sort(sample_array)
    print("Отсортированный массив:", sorted_array)
