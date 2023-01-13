def get_numbers(my_string):
    """
    This function will run through the strings that contains digits and will separate and return them
    :return: Digits that are within the string
    """
    digits = ""
    for char in my_string:
        if char.isdigit():
            digits += char
    return digits
