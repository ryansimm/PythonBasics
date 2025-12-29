#Task is to receive name and birth year, then calucalte
# their age and print a personalised message.

name = input("Please enter your name: ")
birth_year = int(input("Please enter your year of birth: "))
current_year = int(input("Please enter the current year: "))
age = current_year - birth_year
birthplace = input("Please enter your place of birth: ")
home = input("Where do you currently call home? ")

print(f"Hello {name}, you are {age} years old. You were born in {birthplace} and currently stay in {home}.")