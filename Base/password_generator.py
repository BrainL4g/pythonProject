import random
import string  # модуль string для доступа к набору символов


def generate_password(length):
    # Функция для генерации пароля заданной длины
    # Создаем строку, содержащую все возможные символы для пароля
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль, выбирая случайные символы из all_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    print(f"Сгенерированный пароль: {password}")
