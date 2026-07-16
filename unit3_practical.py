#calculator.py

#Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Display heading
print("\n======== Calculator Results ========")

#Addition
print(f"Subtraction    : {round(num1 + num2)}")

#Subtraction
print(f"Subtraction    : {round(num1 - num2)}")

#Multiplication
print(f"Multiplication : {round(num1 * num2)}")

# Check for division by zero
if num2 != 0:
   print(f"Divison   : {round(num1 / num2, 2)}")
   print(f"Floor Division   : {round(num1 // num2, 2)}")
   print(f"Modulus    : {round(num1 % num2, 2)}")
else:
   print("Division     : Cannot divide by zero.")
   print("Floor Division :Cannot divide by zero.")
   print("Modulus        : Cannot divide by zero.")