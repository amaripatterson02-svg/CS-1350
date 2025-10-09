# Grade Book System

def add_student(gradebook, name, grade):
    # Check if the grade is within valid range
    if 0 <= grade <= 100:
        gradebook[name] = grade
        return True
    else:
        return False

def get_class_average(gradebook):
    # Return 0 if gradebook is empty
    if not gradebook:
        return 0
    # Calculate average
    total = sum(gradebook.values())
    avg = total / len(gradebook)
    return avg

# Bonus -- 10 Points
def get_passing_students(gradebook):
    # Return list of names with grade >= 60
    passing = [name for name, grade in gradebook.items() if grade >= 60]
    return passing

# Test your functions
if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85))     # Should print True
    print(add_student(gradebook, "Bob", 150))      # Should print False
    print(add_student(gradebook, "Charlie", 45))   # Should print True

    print(f"Average: {get_class_average(gradebook):.2f}")  # Should print 65.00
    print(f"Passing: {get_passing_students(gradebook)}")   # Should print ['Alice']

