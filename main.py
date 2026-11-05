import random

first_length = int(input("Введите размер первого списка: "))
second_length = int(input("Введите размер второго списка: "))

first_numbers = []
second_numbers = []
result = []

for i in range(first_length):
    first_numbers.append(random.randint(1, 100))

for i in range(second_length):
    second_numbers.append(random.randint(1, 100))

print(f"Первый список: {first_numbers}")
print(f"Второй список: {second_numbers}")

max_length = max(first_length, second_length)

for i in range(max_length):
    first_numbers_element = first_numbers[i] if i < first_length else 0
    second_numbers_element = second_numbers[i] if i < second_length else 0
    result.append(first_numbers_element + second_numbers_element)

print(f"Результат: {result}")