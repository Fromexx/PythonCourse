print("Enter two numbers: ")
a = input()
b = input()

result = 0
try:
    result = int(a) / int(b)
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Division by zero")
else:
    print(result)
finally:
    print("Program ended")