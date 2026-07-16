# Secure Password Hint Tool

#Ask the user for their password
password = input("Enter your secret password: ")

#Remove leading and trailing spaces
password = password.strip()

#Get the first and last characters
first_letter = password[0]
last_letter = password[-1]

#Display the password hint
print(f"Your password hint: It starts with {first_letter.upper()}  and end with {last_letter.upper()}.")