# grade_report.py

students = [
    {
        "name": "Amanda",
        "maths": 78,
        "english": 72,
        "science": 81
    },
    {
        "name": "Bongani",
        "maths": 65,
        "english": 59,
        "science": 68
    },
    {
        "name": "Carol",
        "maths": 92,
        "english": 88,
        "science": 95
    },
    {
        "name": "David",
        "maths": 48,
        "english": 54,
        "science": 45
    },
    {
        "name": "Emma",
        "maths": 35,
        "english": 42,
        "science": 38
    }
]

results = []


def get_grade_and_status(average):
    """Return a grade and status based on the student's average."""

    if average >= 80:
        grade = "A"
        status = "Excellent"
    elif average >= 70:
        grade = "B"
        status = "Very Good"
    elif average >= 60:
        grade = "C"
        status = "Good"
    elif average >= 50:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    return grade, status


def search_student(name):
    """Search for a student in the results list by name."""

    for result in results:
        if result["name"].lower() == name.lower():
            return result

    return None


# Process each student's results
for student in students:
    total = (
        student["maths"]
        + student["english"]
        + student["science"]
    )

    average = total / 3
    grade, status = get_grade_and_status(average)

    result = {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }

    results.append(result)


# Calculate class statistics
total_class_average = 0
all_marks = []

for student in students:
    total_class_average += (
        student["maths"]
        + student["english"]
        + student["science"]
    ) / 3

    all_marks.append(student["maths"])
    all_marks.append(student["english"])
    all_marks.append(student["science"])


class_average = total_class_average / len(students)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)


# Display the class report
print("=" * 64)
print("CLASS GRADE REPORT")
print("=" * 64)

print(
    f"{'Name':<15}"
    f"{'Average':<12}"
    f"{'Grade':<10}"
    f"{'Status':<15}"
)

print("-" * 64)

for result in results:
    print(
        f"{result['name']:<15}"
        f"{result['average']:<12.2f}"
        f"{result['grade']:<10}"
        f"{result['status']:<15}"
    )

print("-" * 64)
print("CLASS STATISTICS")
print("-" * 64)
print(f"Class average : {class_average:.2f}")
print(f"Highest mark  : {highest_mark}")
print(f"Lowest mark   : {lowest_mark}")
print("=" * 64)


# Allow the user to search for students
while True:
    print("\nSTUDENT SEARCH")
    search_name = input(
        "Enter a student's name or type 'exit' to close: "
    ).strip()

    if search_name.lower() == "exit":
        print("Grade report closed.")
        break

    found_student = search_student(search_name)

    if found_student is None:
        print("Student not found.")
    else:
        print("\nStudent found")
        print("-" * 30)
        print(f"Name   : {found_student['name']}")
        print(f"Average: {found_student['average']:.2f}")
        print(f"Grade  : {found_student['grade']}")
        print(f"Status : {found_student['status']}")
        print("-" * 30)