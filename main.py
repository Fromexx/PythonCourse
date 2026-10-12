def max_number(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        return b
    return None


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def test_max_number():
    assert max_number(1, 2) == 2
    assert max_number(1.2, 3.2) == 3.2
    assert max_number(-1, -10) == -1
    assert max_number(2, 2) == 2
    assert max_number(2, "rgrg") is None


for i in even_numbers(10):
    print(i)

test_max_number()
print("Тесты пройдены")