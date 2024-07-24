import re  # Import the regular expression module for pattern matching

def remove_numbers_from_end(file_path):
    """
    Removes numerical values from the end of each line in a text file.

    Args:
        file_path (str): The path to the input/output text file.
    """

    with open(file_path, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_line = re.sub(r"\s+\d+(\.\d+)?$", "", line)  # Remove numbers and optional decimal parts
        modified_lines.append(modified_line)

    with open(file_path, "w") as file:  # Overwrite the original file
        file.writelines(modified_lines)

# Get the file path from the user (you can hardcode it if you prefer)
file_path = "text.txt"

remove_numbers_from_end(file_path)
print("Numerical values removed successfully!")