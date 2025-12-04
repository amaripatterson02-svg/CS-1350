def count_lines(filename):
    """
    Read a file and return the number of lines.
    If the file doesn't exist, return -1.
    """
    try:
        with open(filename, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return -1
