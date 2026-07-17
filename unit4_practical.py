# grade_classifier.py

# Collect learner details
name = input("Enter learner name: ")
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Assign grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check for intervention
interventions = []

if mark1 < 40:
    interventions.append("Subject 1 needs intervention")
if mark2 < 40:
    interventions.append("Subject 2 needs intervention")
if mark3 < 40:
    interventions.append("Subject 3 needs intervention")

# Display report card
print("\n========== REPORT CARD ==========")
print(f"Learner Name: {name}")
print(f"Subject 1 Mark: {mark1}")
print(f"Subject 2 Mark: {mark2}")
print(f"Subject 3 Mark: {mark3}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if interventions:
    print("Intervention Flags:")
    for item in interventions:
        print(f"- {item}")
else:
    print("Intervention Flags: None")

print("=================================")