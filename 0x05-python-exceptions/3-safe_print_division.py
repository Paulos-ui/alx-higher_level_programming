#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError) as e:
        print("Inside result:", e)
        div = None
    return div

a = 10
b = 2
result = safe_print_division(a, b)
print("Outside result:", result)

