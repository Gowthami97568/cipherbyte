def display_menu():
    print("\nContactMaster - Main Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit\n")

# Function to load contacts from a file
def load_contacts(filename="contacts.csv"):
    contacts = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass  # If file doesn't exist, start with empty contact list
    return contacts

# Function to save contacts to a file
def save_contacts(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts.append([name, phone, email])
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nList of Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

# Function to search for a contact by name
def search_contact(contacts):
    search_name = input("Enter the name to search: ")
    found_contacts = [contact for contact in contacts if search_name.lower() in contact[0].lower()]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    else:
        print("No contacts found with that name.")

# Function to update a contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input(f"Enter new name for {contacts[index][0]} (leave blank to keep current): ") or contacts[index][0]
            phone = input(f"Enter new phone number for {contacts[index][0]} (leave blank to keep current): ") or contacts[index][1]
            email = input(f"Enter new email for {contacts[index][0]} (leave blank to keep current): ") or contacts[index][2]
            contacts[index] = [name, phone, email]
            print(f"Contact {name} updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact {deleted_contact[0]} deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

# Main program loop
def contact_master():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# Run the contact management system
if __name__ == "__main__":
    contact_master()
