import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Выбираем опорный элемент
        left = [x for x in arr if x < pivot]  # Элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы равные опорному
        right = [x for x in arr if x > pivot]  # Элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    print("Исходный массив:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Отсортированный массив:", sorted_array)
