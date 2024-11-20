import random


def show_score(attempts_list):
    # Проверяем, есть ли записи о попытках
    if not attempts_list:
        print('В данный момент нет рекорда, он ждет тебя!')
    else:
        # Выводим минимальное количество попыток из списка
        print(f'Текущий рекорд по количеству попыток: {min(attempts_list)} попыток')


def start_game():
    attempts = 0  # Счетчик попыток
    rand_num = random.randint(1, 10)  # Генерация случайного числа от 1 до 10
    attempts_list = []  # Список для хранения количества попыток

    print('Здравствуйте, путешественник! Добро пожаловать в игру угадай число!')
    player_name = input('Как вас зовут? ')  # Запрашиваем имя игрока
    wanna_play = input(f'Привет, {player_name}, хотите поиграть в игру угадай число? (Введите Да/Нет): ')

    # Проверяем, хочет ли игрок играть
    if wanna_play.lower() != 'да':
        print('Хорошо, спасибо!')
        exit()  # Выходим из программы, если игрок не хочет играть
    else:
        show_score(attempts_list)  # Показываем текущий рекорд

    # Основной цикл игры
    while wanna_play.lower() == 'да':
        try:
            guess = int(input('Выберите число от 1 до 10: '))  # Запрашиваем число у игрока
            # Проверяем, что число в заданном диапазоне
            if guess < 1 or guess > 10:
                raise ValueError('Пожалуйста, выберите число в заданном диапазоне')

            attempts += 1  # Увеличиваем счетчик попыток

            # Проверяем, угадал ли игрок число
            if guess == rand_num:
                attempts_list.append(attempts)  # Добавляем количество попыток в список
                print('Отлично! Вы угадали!')
                print(f'На это у вас ушло {attempts} попыток')
                wanna_play = input('Хотите сыграть еще раз? (Введите Да/Нет): ')

                # Проверяем, хочет ли игрок сыграть еще раз
                if wanna_play.lower() != 'да':
                    print('Хорошо, хорошего дня!')
                    break  # Выходим из цикла, если игрок не хочет играть снова
                else:
                    attempts = 0  # Сбрасываем счетчик попыток
                    rand_num = random.randint(1, 10)  # Генерируем новое случайное число
                    show_score(attempts_list)  # Показываем текущий рекорд
                    continue  # Продолжаем цикл
            else:
                # Подсказываем игроку, больше или меньше загаданное число
                if guess > rand_num:
                    print('Загаданное число меньше')
                elif guess < rand_num:
                    print('Загаданное число больше')

        except ValueError as err:
            # Обрабатываем ошибки ввода
            print('Ой, это не корректное значение. Попробуйте снова...')
            print(err)


if __name__ == '__main__':
    start_game()