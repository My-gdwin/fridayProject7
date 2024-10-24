def get_input(prompt):
    """
    This function prompts the user for input and returns the user's response.
    """
    return input(prompt)

def main():
    # Instructions for the player
    print("Welcome to the Mad Libs game! Please follow the instructions and provide the words when prompted.\n")

    # Getting the necessary words from the user
    large_object = get_input("Enter a large object: ")
    large_objects_plural = get_input("Enter large objects (plural): ")
    adjective = get_input("Enter an adjective: ")
    body_part = get_input("Enter a body part: ")
    restaurant = get_input("Enter a restaurant: ")
    food_1 = get_input("Enter a food: ")
    food_2 = get_input("Enter another food: ")

    # The story template with placeholders filled in by user input
    story = f"""
    I’ve had a very {adjective} day.
    This morning, I dropped a box of {large_objects_plural} on my {body_part}.
    Then, at lunch, I went to {restaurant} for their delicious {food_1},
    But the waiter brought me {food_2}, which I was not hungry for.
    Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.
    """

    # Print the generated story
    print("\nHere's your Mad Lib story:\n")
    print(story)

# Run the main function
if __name__ == "__main__":
    main()
