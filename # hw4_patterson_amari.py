# hw4_patterson_amari.py
# CS1350 - OOP Module Homework Assignment 1
# Classes, Encapsulation, and Inheritance
# Author: Amari Patterson

# ============================
# Problem 1: Bank Account Hierarchy
# ============================

class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Error: Deposit amount must be positive.")
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")
        return self._balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner} - Balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    def withdraw(self, amount):
        if self._balance - amount < 100:
            print("Cannot go below $100 minimum")
        else:
            super().withdraw(amount)


# ============================
# Problem 2: Student Management System (Bonus)
# ============================

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print("Error: Invalid grade. Must be between 0 and 100.")

    @property
    def gpa(self):
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def get_letter_grade(self):
        if not self._grades:
            return "N/A"
        avg = self.gpa
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - GPA: {self.gpa:.1f}"


class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic

    def get_letter_grade(self):
        if not self._grades:
            return "N/A"
        avg = self.gpa
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        else:
            return "F"


class HonorsStudent(Student):
    def __init__(self, name, student_id, honors_thesis=None):
        super().__init__(name, student_id)
        self.honors_thesis = honors_thesis

    @property
    def is_eligible_for_honors(self):
        return self.gpa >= 87.5

    def set_thesis(self, topic):
        if self.is_eligible_for_honors:
            self.honors_thesis = topic
        else:
            print("Not eligible for honors thesis")


class StudentRoster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def list_honor_roll(self):
        for s in self.students:
            if s.gpa >= 85:
                print(f"{s.name} - GPA: {s.gpa:.1f}")

    def class_average(self):
        if not self.students:
            return 0.0
        total = sum(s.gpa for s in self.students)
        return total / len(self.students)


# ============================
# TESTING SECTION
# ============================
if __name__ == "__main__":
    # Test Problem 1
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")

    print("\n" + "=" * 40 + "\n")

    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    savings.withdraw(950)  # Should fail
    savings.withdraw(500)  # Should work
    print(f"Final balance: ${savings.balance}")

    print("\n" + "=" * 40 + "\n")

    # Test Problem 2 (Bonus)
    roster = StudentRoster()

    s1 = Student("Alice", "001")
    s1.add_grade(92)
    s1.add_grade(88)
    s1.add_grade(95)

    s2 = GraduateStudent("Bob", "002", "Machine Learning")
    s2.add_grade(85)
    s2.add_grade(82)

    s3 = HonorsStudent("Carol", "003")
    s3.add_grade(95)
    s3.add_grade(98)
    s3.add_grade(92)

    roster.add_student(s1)
    roster.add_student(s2)
    roster.add_student(s3)

    print("All Students:")
    for student in [s1, s2, s3]:
        print(f" {student} - Grade: {student.get_letter_grade()}")

    print("\nHonor Roll:")
    roster.list_honor_roll()

    print(f"\nClass Average: {roster.class_average():.1f}")

    s3.set_thesis("Advanced Algorithms")
    print(f"\nCarol's thesis: {s3.honors_thesis}")