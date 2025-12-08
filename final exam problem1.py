def count_lines_with_word(filename, word):
    """
    Count how many lines in a file contain a specific word.
    The search should be case-insensitive.

    Returns 0 if file doesn't exist.
    """
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                if word.lower() in line.lower():
                    count += 1
    except FileNotFoundError:
        return 0

    return count
