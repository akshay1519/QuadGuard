class Password:
    def __init__(self):
        pass

    def check_password_strength(self, password):
        # List to store error messages
        errorsValidation = []
        # Check if password is at least 8 characters long
        if len(password) < 8:
            errorsValidation.append("Password should be at least 8 characters long")
        # Check if password has at least one numeral
        if not any(char.isdigit() for char in password):
            errorsValidation.append("Password should have at least one numeral")
        # Check if password has at least one uppercase letter
        if not any(char.isupper() for char in password):
            errorsValidation.append("Password should have at least one uppercase letter")
        # Check if password has at least one lowercase letter
        if not any(char.islower() for char in password):
            errorsValidation.append("Password should have at least one lowercase letter")
        # Check if password has at least one special character letter
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
            errorsValidation.append("Password should have at least one special character")
        # return True if all conditions are met
        return errorsValidation
    

