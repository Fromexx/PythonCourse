real_password = "admin"
entered_password = ""

while entered_password != real_password:
    entered_password = input("Введите пароль: ")
    print("Вход разрешен!" if entered_password == real_password else "Неверно, повторите попытку")