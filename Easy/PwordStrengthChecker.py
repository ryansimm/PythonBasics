password = input("please enter your password so I can check the strength: ")
length = len(password)
has_upper = any(character.isupper() for character in password)
has_lower = any(character.islower() for character in password)
has_numbers = any(character.isdigit() for character in password)
special_characters = "!@#$%^&*()-+?"
has_special = any(character in special_characters for character in password)
strength = 0
if length >= 8:
    strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_numbers:
        strength += 1
    if has_special:
        strength += 1  

print(f"Your password strength is {strength} out of 5.")