def calculate_average(grades):
    return sum(grades) / len(grades)


def add_student(name, grades):
    students.append({"name": name, "grades": grades})
    calculate_class_average()


def remove_student(student_index):
    removed_student = students.pop(student_index)
    calculate_class_average()
    return removed_student


def calculate_class_average():
    common_average = 0

    for student in students:
        average = calculate_average(student["grades"])
        common_average += average
        print(
            f"Студент: {student["name"]}: средний балл: {average:.2f}, статус: {"Успешный" if average >= 75 else "Отстающий"}")

    print(f"\nОбщий средний балл: {common_average / len(students):.2f}\n")


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

calculate_class_average()

print(f"Добавлен студент: Froms")
add_student("Froms", [66, 100, 94])

lowest_average = calculate_average(students[0]["grades"])
lowest_average_index = 0

for i in range(1, len(students)):
    current_average = calculate_average(students[i]["grades"])

    if current_average < lowest_average:
        lowest_average = current_average
        lowest_average_index = i
    if i == len(students) - 1:
        print("Удаление студента с самым низким средним баллом")
        removed_student = remove_student(lowest_average_index)
        print(f"Был удален студент: {removed_student['name']} (Средний балл: {lowest_average:.2f})")