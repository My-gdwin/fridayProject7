    # Importing the random module to use the randint function
import random

def generate_lottery_numbers():
    """
    This function generates a PowerBall ticket by picking 5 random numbers 
    between 1 and 69 (white balls) and 1 random number between 1 and 26 (red ball).
    """
    # Generate 5 unique random numbers for the white balls (1-69)
    white_balls = random.sample(range(1, 70), 5)
    # Sort the white ball numbers to simulate the official ticket order
    white_balls.sort()

    # Generate the red ball number (1-26)
    red_ball = random.randint(1, 26)

    # Return the white ball numbers and the red ball number
    return white_balls, red_ball

def main():
    # Greeting message
    print("Welcome to the PowerBall Lottery Number Generator!")

    # Generate lottery numbers
    white_balls, red_ball = generate_lottery_numbers()

    # Format and print the results
    # First five white balls separated by one space, followed by three spaces before the red ball
    print("\nYour PowerBall numbers are:")
    print(" ".join(map(str, white_balls)) + "   " + str(red_ball))

    # Farewell message
    print("\nGood luck! Thanks for using the PowerBall Lottery Number Generator!")

# Run the main function
if __name__ == "__main__":
    main()
