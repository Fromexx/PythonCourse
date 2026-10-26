real_password = "admin"

while True:
    entered_password = input("Введите пароль: ")
    if entered_password == real_password:
        break
    print("Неверно, повторите попытку")

print("Вход разрешен!")