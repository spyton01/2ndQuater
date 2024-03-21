import sqlite3

# ANSI escape codes for terminal text colors
CORRECT_COLOR = '\033[38;2;0;225;0m'  # Green
WRONG_COLOR = '\033[38;2;225;0;0m'     # Red
RESET_COLOR = '\033[0m'                 # Reset color

def fetch_questions(topic):
    # Create connection to the SQLite database
    connection = sqlite3.connect('QuestionsAnswer1.db')
    cursor = connection.cursor()

    # Fetching questions and answers from the specified table
    cursor.execute(f'SELECT id, questions, answers FROM {topic}')
    questions = cursor.fetchall()

    # Closing the database connection
    connection.close()

    return questions

def main():
    # Asking user to input the topic
    topic = input("Enter the topic ('OCM_Logistic', 'Modern_History', 'Finance', 'Business_Analytics', 'Prog_Logic'): ")

    # Fetching questions related to the specified topic
    questions = fetch_questions(topic)

    if questions:
        print(f"Here are the questions for the topic '{topic}':")
        score = 0
        total_questions = len(questions)

        # Iterating through each question
        for qid, question, answer in questions:
            print(f"Question {qid}: {question}")
            # Prompting user for their answer
            user_answer = input("Your answer: ").strip().upper()

            # Checking if the user's answer is correct
            if user_answer == answer:
                print(CORRECT_COLOR + "Correct!" + RESET_COLOR)
                score += 1
            else:
                # Displaying correct answer if user's answer is wrong
                print(WRONG_COLOR + f"Wrong! Correct answer is {answer}" + RESET_COLOR)

        # Displaying the quiz score
        print(f"\nQuiz done! You scored {score}/{total_questions}")
    else:
        # Informing user if no questions found for the specified topic
        print("No questions found for the specified topic.")

if __name__ == "__main__":
    main()