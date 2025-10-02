import numpy as np
import time

np.random.seed(1350)

# ---------------- Problem 1 ----------------
def problem1():
    """
    Array creation and basic operations
    """

    # a) 1D array of integers from 10 to 50 (inclusive) with step 5
    arr1 = np.arange(10, 55, 5)

    # b) 2D array of shape (3, 4) filled with zeros
    arr2 = np.zeros((3, 4))

    # c) 3x3 identity matrix
    identity = np.eye(3)

    # d) 10 evenly spaced numbers between 0 and 5
    linspace_arr = np.linspace(0, 5, 10)

    # e) Random array of shape (2, 5) with values between 0 and 1
    random_arr = np.random.rand(2, 5)

    return arr1, arr2, identity, linspace_arr, random_arr

# ---------------- Problem 2 ----------------
def problem2():
    """
    Broadcasting and array mathematics
    """
    arr_a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
    arr_b = np.array([10, 20, 30])

    # a) Add arr_b to each row of arr_a
    result_add = arr_a + arr_b

    # b) Multiply each column of arr_a by the corresponding element in arr_b
    result_multiply = arr_a * arr_b

    # c) Square all elements
    result_square = arr_a ** 2

    # d) Mean of each column
    column_means = arr_a.mean(axis=0)

    # e) Centering
    centered_arr = arr_a - column_means

    return result_add, result_multiply, result_square, column_means, centered_arr

# ---------------- Problem 3 ----------------
def problem3():
    """
    Indexing and slicing
    """

    arr = np.arange(1, 26).reshape(5, 5)

    # a) Third row
    third_row = arr[2, :]

    # b) Last column
    last_column = arr[:, -1]

    # c) 2x2 subarray from center (rows 1-2, cols 1-2 → using indices 1:3)
    center_subarray = arr[1:3, 1:3]

    # d) All elements > 15
    greater_than_15 = arr[arr > 15]

    # e) Replace evens with -1
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1

    return third_row, last_column, center_subarray, greater_than_15, arr_copy

# ---------------- Problem 4 ----------------
def problem4():
    """
    Statistical analysis
    """
    scores = np.array([[85, 90, 78, 92],
                       [79, 85, 88, 91],
                       [92, 88, 95, 89],
                       [75, 72, 80, 78],
                       [88, 91, 87, 94]])

    # a) Average per student
    student_averages = scores.mean(axis=1)

    # b) Average per test
    test_averages = scores.mean(axis=0)

    # c) Highest score per student
    student_max_scores = scores.max(axis=1)

    # d) Standard deviation per test
    test_std = scores.std(axis=0)

    # e) Students with avg > 85
    high_performers = student_averages > 85

    return student_averages, test_averages, student_max_scores, test_std, high_performers

# ---------------- Problem 5 ----------------
def problem5():
    """
    Performance comparsion between Python lists and NumPy
    """
    size = 100000

    python_list = list(range(size))
    numpy_array = np.arange(size)

    # Python list timing
    start_time = time.time()
    list_result = [x ** 2 for x in python_list]
    list_time = time.time() - start_time

    # NumPy timing
    start_time = time.time()
    array_result = numpy_array ** 2
    numpy_time = time.time() - start_time

    speedup = list_time / numpy_time

    return {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
    }

# ---------------- Run Tests ----------------
if __name__ == "__main__":
    print("Problem 1:", problem1())
    print("Problem 2:", problem2())
    print("Problem 3:", problem3())
    print("Problem 4:", problem4())
    print("Problem 5:", problem5())