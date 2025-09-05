"""
Contact Management System - Homework 1
Student: Patterson, Amari
Course: CS1350
Week 1 Assignment
"""

from datetime import datetime

# Global database (dictionary)
contacts_db = {}


# ---------- Part 1: Core Contact Management ----------

def create_contact() -> dict:
    """
    Prompt the user to create a new contact dictionary.
    Required: first_name, last_name, phone
    Optional: email, address, category, notes
    Returns:
        dict: Contact data
    """
    # TODO: implement input prompts & validation
    pass


def add_contact(contacts_db: dict, contact_data: dict) -> str | None:
    """
    Add a new contact to the database.
    Args:
        contacts_db (dict): main database
        contact_data (dict): contact info
    Returns:
        str: generated contact ID, or None
    """
    pass


def display_contact(contacts_db: dict, contact_id: str) -> bool:
    """Display one contact by ID."""
    pass


def list_all_contacts(contacts_db: dict):
    """List all contacts (ID, name, phone)."""
    pass


# ---------- Part 2: Advanced Operations ----------

def search_contacts_by_name(contacts_db: dict, search_term: str) -> dict:
    """Search by first or last name (partial, case-insensitive)."""
    pass


def search_contacts_by_category(contacts_db: dict, category: str) -> dict:
    """Find contacts in a given category."""
    pass


def find_contact_by_phone(contacts_db: dict, phone_number: str) -> tuple:
    """Find a contact by exact phone number."""
    pass


def update_contact(contacts_db: dict, contact_id: str, field_updates: dict) -> bool:
    """Update specific fields and last_modified timestamp."""
    pass


def delete_contact(contacts_db: dict, contact_id: str) -> bool:
    """Delete a contact with confirmation."""
    pass


def merge_contacts(contacts_db: dict, contact_id1: str, contact_id2: str) -> str | None:
    """Merge two contacts, keeping the most recent info."""
    pass


def generate_contact_statistics(contacts_db: dict) -> dict:
    """
    Generate database stats:
      - total_contacts
      - contacts_by_category
      - contacts_by_state
      - average_contacts_per_category
      - most_common_area_code
      - contacts_without_email
    """
    pass


def find_duplicate_contacts(contacts_db: dict) -> dict:
    """Find duplicates by phone, email, or name."""
    pass


def export_contacts_by_category(contacts_db: dict, category: str) -> str:
    """Export formatted contacts by category."""
    pass


# ---------- Part 3: User Interface ----------

def save_contacts_to_file(contacts_db: dict, filename: str):
    """Save contacts to text file."""
    pass


def load_contacts_from_file(filename: str) -> dict:
    """Load contacts from text file."""
    return {}


def main_menu():
    """Display and handle main menu options."""
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add new contact")
        print("2. Search contacts by name")
        print("3. List all contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Generate statistics")
        print("7. Find duplicates")
        print("8. Export by category")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            print("TODO: implement add contact")
        elif choice == "2":
            print("TODO: implement search")
        elif choice == "3":
            print("TODO: implement list contacts")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Option not implemented yet.")


def run_contact_manager():
    """Main entry point."""
    global contacts_db
    contacts_db = {}
    print("Welcome to the Contact Manager!")
    main_menu()


# ---------- Script entry ----------
if __name__ == "__main__":
    run_contact_manager()
