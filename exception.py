try:
    name= input("Please enter your name:")
    family_name= input("Please enter your family name:")
    age= input("Please enter your age:")
    if len(name)< 2:
        raise ValueError("Please enter your full name.")
    elif not name.isalpha():
        raise ValueError("Please enter your correct name.")
    if len(family_name)< 2:
        raise ValueError("Please enter your full family name.")
    elif not family_name.isalpha():
        raise ValueError("Please enter your correct family name.")
    age_error= int(age)
    print("Information accepted.")
except ValueError as e:
    print(f"error: {e}")