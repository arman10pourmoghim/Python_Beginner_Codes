password= input("Please enter your password: ")
def check(password):
    special_char= "!@#$%^&*()-_=+[{]}|;:'\",<.>/?"
    length= False
    upper= False
    lower= False
    digit= False
    special= False
    if len(password)< 8:
        print("Password must be at least 8 characters long.")
        return False
    for char in password:
        if "A" <= char <= "Z":
            upper= True
        elif "a" <= char <= "z":
            lower= True
        elif "0" <= char <= "9":
            digit= True
        elif char in special_char:
            special= True
    if not upper:
        print("Password must contain at least one uppercase letter.")
        return False
    elif not lower:
        print("Password must contain at least one lowercase letter.")
        return False
    elif not digit:
        print("Password must contain at least one digit.")
        return False
    elif not special:
        print("Password must contain at least one special character.")
        return False
    print("Password is valid.")
    return True
check(password)