CHECKING_PASSWORD = input("Введите пароль для проверки: ")


def pass_characteristics(pass_letters, pass_length):
    score = 0
    print("Проверка надежности пароля:")

    if not any(letter.isdigit() for letter in pass_letters):
        return print("Пароль не содержит цифр")
    score = score + 2

    if pass_length < 12:
        return print("Пароль слишком короткий")
    score = score + 2

    if not any(letter.isupper() for letter in pass_letters):
        return print("Пароль не содержит заглавных букв")
    score = score + 2

    if not any(letter.islower() for letter in pass_letters):
        return print("Пароль не содержит строчных букв")
    score = score + 2

    if all(letter.isalnum() for letter in pass_letters):
        return print("Пароль не содержит специальных символов")
    score = score + 2

    print(f"Надежность пароля: {score} очков")
    return score


def main():
    pass_letters = list(CHECKING_PASSWORD)
    pass_length = len(CHECKING_PASSWORD)
    print(f"В пароле {pass_length} символов.")
    pass_characteristics(pass_letters, pass_length)


if __name__ == '__main__':
    main()
