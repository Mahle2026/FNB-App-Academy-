#Fuel Cost Calculator

#Get user input
kilometers = float(input("Enter the number of kilometers you want to drive: "))
petrol_price = float(input("Enter the current petrol price per liter(R): "))

#Calculate liters
liters_needed = kilometers/ 10

#Calculate total cost
total_cost = liters_needed * petrol_price

#Display the results
print("\n==== Fuel Cost Calculator ====")
print(f"Distance: {kilometers} km")
print(f"Petrol Price: R{petrol_price}")
print(f"Fuel Needed: {round(liters_needed, 2)}")
print(f"Total Fuel Cost: R{round(total_cost, 2)}")