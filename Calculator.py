def request_data():
    while True:
        try:
            first_number = int(input("Введите первое число: "))
            second_number = int(input("Введите второе число: "))
        except ValueError:
            print("Неправильные данные, введите заново")
        else:
            break

    return first_number, second_number

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        result = "Деление на ноль запрещено"

    return result

print("# Сложение")
first_number, second_number = request_data()
result = add(first_number, second_number)
print(f"Результат сложения: {result}")

print("# Вычитание")
first_number, second_number = request_data()
result = subtract(first_number, second_number)
print(f"Результат вычитания: {result}")

print("# Умножение")
first_number, second_number = request_data()
result = multiply(first_number, second_number)
print(f"Результат умножения: {result}")

print("# Деление")
first_number, second_number = request_data()
result = divide(first_number, second_number)
print(f"Результат деления: {result}")
