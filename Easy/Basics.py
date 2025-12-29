Name = str()
Name = input("Enter your name: ")
age = float(input("Please enter your age: "))
print("Hello " + Name + ", you are " + str(age) + " years old.")
print("Age data type is " + str(type(age)))
print("Name data type is " + str(type(Name)))
if age <= 18:
    print("You are a minor.")
else:
    print("You are an adult.")

print("You will be 100 in " + str(100-age) + " years.")