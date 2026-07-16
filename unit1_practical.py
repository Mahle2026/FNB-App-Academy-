# student_info.py

#Collect user information
first_name = input("Enter your first_name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

#Full Name
full_name = f"{first_name} {surname}"

#Greeting
print(f"\nWelcome, {full_name}!")

#Name formatting
print(f"Name in UPPERCASE: {full_name.upper()}")
print(f"Name in Title Case: {full_name.title()}")

#Age in months
age_months = age * 12
print(f"Age in months: {age_months}")

#Round favourite number
print(f"Favourite number: {favourite_number: .2}")

#Data types
print("\nData Types:")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")
