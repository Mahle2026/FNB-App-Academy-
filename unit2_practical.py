#string_formatter.py

#Collect user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio  = input("Enter a short bio: ")

#Create username
username = (first_name[0] + last_name).lower()

#Format full name
full_name = f"{first_name} {last_name}".title()

#Clean Bio
bio_length = len(bio)

#Replace "I am" with "I'm"
formatted_bio = bio.replace("I am", "I'm")

#Displat the formatted profile
print("\n=== User Profile ===")
print(f"Full Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {formatted_bio}")
print(f"Bio Length: {bio_length} characters")