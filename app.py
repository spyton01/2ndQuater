import sqlite3

#codes for color formatting
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'  # End formatting

def fetch_questions(topic):
    # Connect to the database
    connection = sqlite3.connect('QuestionsAnswer1.db')
    cursor = connection.cursor()

    # Fetch questions for the specified topic
    cursor.execute(f'SELECT id, questions, answers FROM {topic}')
    questions = cursor.fetchall()

    # Close the connection
    connection.close()

    return questions

def main():
    # Specify the topic for which you want to fetch questions
    topic = input("Enter the topic (e.g., 'OCM_Logistic', 'Modern_History', 'Finance', 'Business_Analytics', 'Prog_Logic'): ")

    # Fetch questions for the specified topic
    questions = fetch_questions(topic)

    if questions:
        print(f"Here are the questions for the topic '{topic}':")
        score = 0
        total_questions = len(questions)

        # Iterate over each question
        for qid, question, answer in questions:
            print(f"Question {qid}: {question}")
            user_answer = input("Your answer: ").strip().upper()

            # Check if the answer is correct
            if user_answer == answer:
                print(f"{GREEN}Correct!{END}")
                score += 1
            else:
                print(f"{RED}Wrong! Correct answer is {answer}{END}")

        print(f"\nQuiz done! You scored {score}/{total_questions}")
    else:
        print("No questions found for the specified topic.")

if __name__ == "__main__":
    main()