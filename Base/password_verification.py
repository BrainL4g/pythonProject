def check_password_strength(password):
    # Инициализация счетчиков
    lower_count = sum(1 for c in password if c.islower())  # Количество строчных букв
    upper_count = sum(1 for c in password if c.isupper())  # Количество заглавных букв
    num_count = sum(1 for c in password if c.isdigit())    # Количество цифр
    wspace_count = sum(1 for c in password if c.isspace()) # Количество пробелов
    special_count = sum(1 for c in password if not c.isalnum() and not c.isspace()) # Количество спецсимволов

    # Оценка силы пароля
    strength = 0
    if len(password) >= 8:  # Минимальная длина пароля
        strength += 1
    if lower_count > 0:
        strength += 1
    if upper_count > 0:
        strength += 1
    if num_count > 0:
        strength += 1
    if special_count > 0:
        strength += 1

    # Формирование комментариев в зависимости от силы пароля
    if strength == 1:
        remarks = ('Это очень плохой пароль. '
                   'Смените его как можно скорее.')
    elif strength == 2:
        remarks = ('Это слабый пароль. '
                   'Вы должны рассмотреть возможность использования более сложного пароля.')
    elif strength == 3:
        remarks = 'Ваш пароль неплох, но его можно улучшить.'
    elif strength == 4:
        remarks = ('Ваш пароль трудно угадать. '
                   'Но вы могли бы сделать его еще более безопасным.')
    elif strength == 5:
        remarks = ('Вот это действительно сильный пароль!!! '
                   'Хакерам не удастся его угадать!')

    # Выводим результаты проверки пароля
    print('Ваш пароль содержит:-')
    print(f'{lower_count} строчных букв')
    print(f'{upper_count} заглавных букв')
    print(f'{num_count} цифр')
    print(f'{wspace_count} пробелов')
    print(f'{special_count} специальных символов')
    print(f'Оценка пароля: {strength} из 5')
    print(f'Комментарии: {remarks}')


def main():
    print("Добро пожаловать в проверку пароля!")
    password = input("Пожалуйста, введите ваш пароль для проверки: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
