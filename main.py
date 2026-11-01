total = 0
i = 0
iteration_count = 100 / 2

while i <= iteration_count:
    total += i * 2
    i += 1

print(f"Сумма всех четных чисел от 0 до 100: {total}")


squares = [i ** 2 for i in range(10) if i % 2 != 0]

print(squares)

number = 0
i = 0

while number >= 0:
    number = int(input("Введите число: "))
    i += 1

    if number < 0:
        print(f"Вы ввели отрицательное число, вам потребовалось {i} попыток" )