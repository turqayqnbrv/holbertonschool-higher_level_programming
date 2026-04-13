#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_val = 0

    for char in roman_string:
        current_val = roman_dict.get(char, 0)
        if current_val > prev_val:
            # Subtract twice the previous since it was added once before
            total += current_val - 2 * prev_val
        else:
            total += current_val
        prev_val = current_val

    return total
