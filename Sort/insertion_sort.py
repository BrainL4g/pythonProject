import random


def insertion_sort(arr):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше ключа, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    print("Исходный массив:", sample_array)
    sorted_array = insertion_sort(sample_array)
    print("Отсортированный массив:", sorted_array)
