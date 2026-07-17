#Phone Directory Search

#Create contact dictionary
contacts = {
  "Amahle": "0814578056",
  "Lebo": "0784563870",
  "Joe": "0678356939"
}

#Ask user for a name
name = input("Enter friend's name to search: ")

#Check if name exists in dictionary
if name in contacts:
  print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")