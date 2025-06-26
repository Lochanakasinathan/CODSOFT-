contacts = []

# Add Contact: Allow users to add new contacts with their details.
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully.")

# View Contact List: Display names and phone numbers of all contacts.
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for c in contacts:
            print("Name:", c["name"], "| Phone:", c["phone"])

# Search Contact: Find contacts by name or phone number.
def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for c in contacts:
        if c["name"] == keyword or c["phone"] == keyword:
            print("\nContact Found:")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            found = True
            break
    if not found:
        print("Contact not found.")

# Update Contact: Enable users to update contact details.
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c["name"] == name:
            c["phone"] = input("Enter new phone number: ")
            c["email"] = input("Enter new email: ")
            c["address"] = input("Enter new address: ")
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Delete Contact: Provide an option to delete a contact.
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c["name"] == name:
            contacts.remove(c)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# User Interface: User-friendly menu for interaction
def menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Start the Contact Book
menu()
