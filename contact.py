class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """Add a new contact"""
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }

        print("Contact added successfully!")

    def view_contacts(self):
        """Display all contacts"""
        if not self.contacts:
            print("No contacts found!")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone Number: {details['phone_number']}")
                print("------------------------")

    def search_contact(self):
        """Search for a contact by name or phone number"""
        search_term = input("Enter name or phone number to search: ")

        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["phone_number"]:
                print(f"Name: {name}")
                print(f"Phone Number: {details['phone_number']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                return

        print("Contact not found!")

    def update_contact(self):
        """Update an existing contact"""
        name = input("Enter contact name to update: ")

        if name in self.contacts:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            self.contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address
            }

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        """Delete a contact"""
        name = input("Enter contact name to delete: ")

        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()