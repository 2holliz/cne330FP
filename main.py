#CNE330 Final Project
import random  # Import the random module to use later


# Custom function to get a random number between two values
def my_random(start, end):
    return random.randint(start, end)


# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Pick a random number
target_number = my_random(1, 100)
attempts = 0  # Count how many guesses the player makes

# Game loop
while True:
    guess = input("Enter your guess: ")  # Ask the user for a guess

    if guess.isdigit():  # Check if the input is a number
        guess = int(guess)  # Convert the input to an integer
        attempts += 1  # Add 1 to the attempts

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break  # Exit the loop when the guess is correct
    else:
        print("Please enter a valid number.")  # Warn if input is not a number

# End message
print("Thanks for playing!")