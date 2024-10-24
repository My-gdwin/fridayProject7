# Define a dictionary containing trivia questions as keys and their correct answers as values
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which element has the chemical symbol 'O'?": "Oxygen",
    "What year did the Titanic sink?": "1912"
}

def main():
    # Greet the user
    print("Welcome to the Trivia Quiz!\n")

    # Using a for loop to iterate through the dictionary of questions
    for question, correct_answer in trivia_questions.items():
        # Display the question to the user
        print(question)
        
        # Get the user's answer
        user_answer = input("Your answer: ").strip()

        # Check if the user's answer matches the correct answer (case-insensitive comparison)
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")  # If the answer is correct, print a positive message
        else:
            # If the answer is incorrect, display the correct answer
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

    # Farewell message after the quiz is completed
    print("Thanks for playing the Trivia Quiz! Goodbye!")

# Run the main function
if __name__ == "__main__":
    main()
