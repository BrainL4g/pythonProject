import time


def countdown(user_time):
    bar_length = 50  # Фиксированная длина прогресс-бара

    for remaining in range(user_time, -1, -1):  # Обратный отсчет от user_time до 0
        mins, secs = divmod(remaining, 60)  # Делим общее время на минуты и секунды
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Форматируем время в виде MM:SS

        # Рассчитываем заполненную часть прогресс-бара
        filled_length = int((user_time - remaining) / user_time * bar_length) if user_time > 0 else bar_length

        # Выводим таймер и прогресс-бар в одном сообщении
        print(f'\r{timer} | [{"#" * filled_length}{"." * (bar_length - filled_length)}]',
              end='')  # Используем \r для перезаписи строки
        time.sleep(1)  # Задержка на 1 секунду

    print(f'\r{timer} | [{"#" * bar_length}]')  # Заполняем прогресс-бар полностью в конце
    print('\nСтарт!')


if __name__ == '__main__':
    user_time = int(input("Введите время в секундах: "))
    countdown(user_time)