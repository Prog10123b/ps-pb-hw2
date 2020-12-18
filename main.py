usr_input = input("Введите пароль: ") + "0"

try:
    numeric_input = int(usr_input)
    1 / numeric_input
    print("Ваш пароль состоит только из цифр")
except ValueError:
    print("Требования к паролю соблюдены")
except ZeroDivisionError:
    print("Вы ввели пустой пароль")