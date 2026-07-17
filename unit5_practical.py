# contact_book.py

contacts = []


def add_contact():
    """Add a new contact to the contact list."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"\n{name} was added successfully.\n")


def search_contact(name):
    """Search for a contact by name and return the contact dictionary."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None


def delete_contact(name):
    """Delete a contact by name."""
    contact = search_contact(name)

    if contact is None:
        print("\nContact not found.\n")
        return

    contacts.remove(contact)
    print(f"\n{name} was deleted successfully.\n")


def display_contact(contact):
    """Display one contact in a formatted layout."""
    print("-" * 35)
    print(f"Name : {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print("-" * 35)


def view_all():
    """Display all saved contacts."""
    if not contacts:
        print("\nNo contacts have been added yet.\n")
        return

    print("\nContact List")

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        display_contact(contact)

    print()


def show_menu():
    """Display the contact book menu."""
    print("CONTACT BOOK")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_name = input("Enter the name to search: ").strip()
        found_contact = search_contact(search_name)

        if found_contact is None:
            print("\nContact not found.\n")
        else:
            print("\nContact found:")
            display_contact(found_contact)
            print()

    elif choice == "3":
        delete_name = input("Enter the name to delete: ").strip()
        delete_contact(delete_name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("\nContact book closed.")
        break

    else:
        print("\nInvalid option. Please choose a number from 1 to 5.\n")