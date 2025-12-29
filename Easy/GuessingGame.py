import random
number = random.randint(1,20)
guess = int(input("Please try guess the random number between 1 and 20:"))
if guess > 20 or guess < 1:
    print("Your guess is out of range. Please guess a number between 1 and 20.")
while guess != number:
        if guess < number:
            print("Too low, try again. ")
        elif guess > number:
            print("Too high, try again. ")
        guess = int(input("Enter your guess: "))
print("Congratulations! You've guessed the correct number:", number)
print("The number was", guess)