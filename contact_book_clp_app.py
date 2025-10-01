import json 
import os 
 
CONTACTS_FILE = "contacts.json" 
 
# Load contacts from a file (if exists) 
def load_contacts(): 
    if os.path.exists(CONTACTS_FILE): 
        with open(CONTACTS_FILE, "r") as f: 
            return json.load(f) 
    return [] 
 
# Save contacts to a file 
def save_contacts(contacts): 
    with open(CONTACTS_FILE, "w") as f: 
        json.dump(contacts, f, indent=4) 
 
# Add new contact 
def add_contact(contacts): 
    name = input("Enter name: ") 
    phone = input("Enter phone: ") 
    email = input("Enter email: ") 
 
    contact = {"name": name, "phone": phone, "email": email} 
    contacts.append(contact) 
    print("Contact added successfully.") 
 
# View all contacts 
def view_contacts(contacts): 
    if not contacts: 
        print("No contacts to show.") 
        return 
    for i, contact in enumerate(contacts, start=1): 
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}") 
 
# Search contact by name 
def search_contacts(contacts): 
    search_name = input("Enter name to search: ").lower() 
    found = [c for c in contacts if search_name in c["name"].lower()] 
 
    if not found: 
        print("No contacts found.") 
    else: 
        for contact in found: 
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}") 
 
# Delete contact by name 
def delete_contact(contacts): 
    name_to_delete = input("Enter the name of the contact to delete: ").lower() 
    updated_contacts = [c for c in contacts if c["name"].lower() != name_to_delete] 
 
    if len(updated_contacts) == len(contacts): 
        print("No contact found with that name.") 
    else: 
        print("Contact deleted.") 
        contacts[:] = updated_contacts  # update original list 
 
# Main loop 
def main(): 
    contacts = load_contacts() 
 
    while True: 
        print("\n--- Contact Book ---") 
        print("1. Add Contact") 
        print("2. View Contacts") 
        print("3. Search Contact") 
        print("4. Delete Contact") 
        print("5. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            add_contact(contacts) 
        elif choice == "2": 
            view_contacts(contacts) 
        elif choice == "3": 
            search_contacts(contacts) 
        elif choice == "4": 
            delete_contact(contacts) 
        elif choice == "5": 
            save_contacts(contacts) 
            print("Goodbye!") 
            break 
        else: 
            print("Invalid choice. Try again.") 
 
if __name__ == "__main__": 
    main() 
 