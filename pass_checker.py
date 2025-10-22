password = input()


def check_length(password):
    return any(len(password) >= 12 for _ in [None])


def check_digits(password):
    return any(letter.isdigit() for letter in password)


def check_uppercase(password):
    return any(letter.isupper() for letter in password)


def check_lowercase(password):
    return any(letter.islower() for letter in password)


def check_specials(password):
    return not password.isalnum()


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
        if check == check_length:
            valid, points = check(password)
            score = score + points
        else:
            if check(password):
                score = score + 2
            else:
                print(f"Ошибка: Пароль не соответствует критерию")
    return score


def main():
    CHECKING_PASSWORD = input("Введите пароль для проверки: ")

    try:
        score = calculate_score(CHECKING_PASSWORD)
        print(f"Надежность пароля: {score} очков")
    except SystemExit:
        print("Проверка пароля завершена с ошибкой")


if name == 'main':
    main()
