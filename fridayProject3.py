# Importing the random module to generate a random number
import random

def main():
    # Greeting the user and asking if they want to play
    print("Welcome to the Number Guessing Game!")
    play_game = input("Do you want to play the game? (yes/no): ").lower()

    # If the user says "no", print a message and exit the program
    if play_game != "yes":
        print("Maybe next time!")
        return  # Exit the program if the user doesn't want to play

    # If the user says "yes", continue with the game
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Start the guessing loop
    while True:
        # Ask the user to guess a number
        guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is too low, too high, or correct
        if guess < secret_number:
            print("Too low! Try again!")
        elif guess > secret_number:
            print("Too high! Try again!")
        else:
            # If the guess is correct, congratulate the user and break the loop
            print("Congratulations! You've guessed the number!")
            break

    # Farewell message after the game is finished
    print("Thanks for playing! Goodbye!")

# Run the main function
if __name__ == "__main__":
    main()
