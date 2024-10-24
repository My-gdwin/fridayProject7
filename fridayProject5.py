# Define functions to change the color of the text using ANSI escape sequences

def red_text(text):
    """
    This function takes a string input and returns the string formatted in red.
    """
    return f"\033[91m{text}\033[0m"  # ANSI code for red text

def blue_text(text):
    """
    This function takes a string input and returns the string formatted in blue.
    """
    return f"\033[94m{text}\033[0m"  # ANSI code for blue text

def green_text(text):
    """
    This function takes a string input and returns the string formatted in green.
    """
    return f"\033[92m{text}\033[0m"  # ANSI code for green text

def yellow_text(text):
    """
    This function takes a string input and returns the string formatted in yellow.
    """
    return f"\033[93m{text}\033[0m"  # ANSI code for yellow text

def brown_text(text):
    """
    This function takes a string input and returns the string formatted in brown (bold).
    """
    return f"\033[33m{text}\033[0m"  # ANSI code for brown (or dark yellow) text

def main():
    # Call each of the functions to demonstrate the color changes
    print(red_text("This is red text."))
    print(blue_text("This is blue text."))
    print(green_text("This is green text."))
    print(yellow_text("This is yellow text."))
    print(brown_text("This is brown text."))

    # Prompt the user for their preferred color and text
    print("\nChoose a color to display your text:")
    print("Options: red, blue, green, yellow, brown")

    # Get the color choice from the user
    user_color = input("Enter a color: ").lower()
    user_text = input("Enter the text you want to display: ")

    # Display the text in the color selected by the user
    if user_color == "red":
        print(red_text(user_text))
    elif user_color == "blue":
        print(blue_text(user_text))
    elif user_color == "green":
        print(green_text(user_text))
    elif user_color == "yellow":
        print(yellow_text(user_text))
    elif user_color == "brown":
        print(brown_text(user_text))
    else:
        print("Sorry, the color you entered is not available.")

# Run the main function
if __name__ == "__main__":
    main()
