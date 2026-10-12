def multiply_numbers(first_number, second_number):
    if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
        return first_number * second_number
    print("Numbers must be an integer")
    return None


print(multiply_numbers(6, 2))