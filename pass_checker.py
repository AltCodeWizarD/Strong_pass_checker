checking_password = input("Введите пароль для проверки:")
pass_letters = list(checking_password)
pass_length = len(checking_password)

print(f"В пароле {pass_length} символов.")


def pass_characteristics(pass_letters, pass_length):
    score = 0
    print("Проверка надежности пароля: ")
    digit_exist = any(letter.isdigit() for letter in pass_letters)
    upper_exist = any(letter.isupper() for letter in pass_letters)
    lower_exist = any(letter.islower() for letter in pass_letters)
    symbols_exist = any(not (letter.isdigit() or letter.isalpha()) for letter in pass_letters)
    if digit_exist:
        score = score + 2
        if pass_length >= 12:
            score = score + 2
            if upper_exist:
                score = score + 2
                if lower_exist:
                    score = score + 2
                    if symbols_exist:
                        score = score + 2
    else:
        print("Пароль не соответствует параметрам")
    print(f"Надежность пароля: {score} очков")


pass_characteristics(pass_letters, pass_length)
