import sys


def check_length(password):
    if len(password) >= 12:
        return True, 2
    print("Ошибка: Пароль слишком короткий (менее 12 символов)")
    sys.exit(1)


def check_digits(password):
    if any(letter.isdigit() for letter in password):
        return True, 2
    print("Ошибка: Пароль не содержит цифр")
    sys.exit(1)


def check_uppercase(password):
    if any(letter.isupper() for letter in password):
        return True, 2
    print("Ошибка: Пароль не содержит заглавных букв")
    sys.exit(1)


def check_lowercase(password):
    if any(letter.islower() for letter in password):
        return True, 2
    print("Ошибка: Пароль не содержит строчных букв")
    sys.exit(1)


def check_specials(password):
    if not password.isalnum():
        return True, 2
    print("Ошибка: Пароль не содержит специальных символов")
    sys.exit(1)


def calculate_score(password):
    checks = [
        check_length,
        check_digits,
        check_uppercase,
        check_lowercase,
        check_specials
    ]

    score = 0
    for check in checks:
        valid, points = check(password)
        score = score + points
    return score


def main():
    CHECKING_PASSWORD = input("Введите пароль для проверки: ")

    try:
        score = calculate_score(CHECKING_PASSWORD)
        print(f"Надежность пароля: {score} очков")
    except SystemExit:
        print("Проверка пароля завершена с ошибкой")


if __name__ == '__main__':
    main()
