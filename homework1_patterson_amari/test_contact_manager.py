"""
Unit tests for Contact Management System
Student: Patterson, Amari 
Course: CS1350
Week 1 Assignment
"""

import unittest
import contact_manager


class TestContactManager(unittest.TestCase):
    """Test cases for the contact manager functions."""

    def setUp(self):
        """Set up a fresh database before each test."""
        self.contacts_db = {}

    # ---------- Part 1: Core Contact Management ----------

    def test_create_contact(self):
        """Test creating a contact (placeholder)."""
        # Example future test:
        # contact = contact_manager.create_contact()
        # self.assertIn("first_name", contact)
        pass

    def test_add_contact(self):
        """Test adding a contact (placeholder)."""
        pass

    def test_display_contact(self):
        """Test displaying a contact (placeholder)."""
        pass

    def test_list_all_contacts(self):
        """Test listing contacts (placeholder)."""
        pass

    # ---------- Part 2: Advanced Operations ----------

    def test_search_contacts_by_name(self):
        """Test searching contacts by name (placeholder)."""
        pass

    def test_search_contacts_by_category(self):
        """Test searching contacts by category (placeholder)."""
        pass

    def test_find_contact_by_phone(self):
        """Test finding contact by phone number (placeholder)."""
        pass

    def test_update_contact(self):
        """Test updating a contact (placeholder)."""
        pass

    def test_delete_contact(self):
        """Test deleting a contact (placeholder)."""
        pass

    def test_merge_contacts(self):
        """Test merging contacts (placeholder)."""
        pass

    def test_generate_contact_statistics(self):
        """Test generating statistics (placeholder)."""
        pass

    def test_find_duplicate_contacts(self):
        """Test finding duplicate contacts (placeholder)."""
        pass

    def test_export_contacts_by_category(self):
        """Test exporting contacts by category (placeholder)."""
        pass


# ---------- Run tests directly ----------
if __name__ == "__main__":
    unittest.main(verbosity=2)
