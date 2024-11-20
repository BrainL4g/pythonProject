import random


def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Меняем местами, если элемент найден больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    print("Исходный массив:", sample_array)
    sorted_array = bubble_sort(sample_array)
    print("Отсортированный массив:", sorted_array)
