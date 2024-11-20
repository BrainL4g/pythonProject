import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Делим массив на две половины
        right_half = arr[mid:]

        merge_sort(left_half)  # Рекурсивно сортируем левую половину
        merge_sort(right_half)  # Рекурсивно сортируем правую половину

        i = j = k = 0

        # Копируем данные во временные массивы left_half и right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы в left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверяем, остались ли элементы в right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    sample_array = [random.randint(1, 100) for _ in range(10)]
    print("Исходный массив:", sample_array)
    sorted_array = merge_sort(sample_array)
    print("Отсортированный массив:", sorted_array)
