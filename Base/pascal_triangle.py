from math import factorial  # Импортируем функцию factorial из модуля math для вычисления факториалов


def pascal_triangle(n):
    # Функция для генерации треугольника Паскаля заданной высоты n
    for i in range(n):
        # Печатаем пробелы для выравнивания треугольника
        for j in range(n - i + 1):
            print(end=' ')

        # Печатаем значения в текущей строке треугольника Паскаля
        for j in range(i + 1):
            # Вычисляем значение элемента треугольника Паскаля по формуле C(i, j) = i! / (j! * (i - j)!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')

        # Переход на новую строку после завершения текущей строки
        print()


if __name__ == '__main__':
    n = int(input("Введите высоту треугольника Паскаля: "))
    pascal_triangle(n)
