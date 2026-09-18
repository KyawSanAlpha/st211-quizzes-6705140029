import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Invlaid email: {email}")
    return True 
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer")
    if age <0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150")
    return True