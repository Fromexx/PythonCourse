import random

length = int(input("Введите размер списков: "))
first_numbers = []
second_numbers = []
result = []

for i in range(length):
    first_numbers.append(random.randint(1, 100))
    second_numbers.append(random.randint(1, 100))

print(f"Первый список: {first_numbers}")
print(f"Второй список: {second_numbers}")

for i in range(length):
    result.append(first_numbers[i] + second_numbers[i])

print(f"Результат: {result}")