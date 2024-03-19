import sqlite3

# create empty database
connect = sqlite3.connect('QuestionsAnswer1.db')
cursor = connect.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS QuestionsAnswer1
               (questions, answers)''')

cursor.execute('SELECT * FROM QuestionsAnswer1')

cursor.execute('''INSERT INTO QuestionsAnswer1 VALUES
                What is the tallest mountain in the world?", "A",
                Who wrote the novel 'To Kill a Mockingbird'?, "B",
                What is the chemical symbol for gold?", "A",
                Who painted 'Starry Night'?", "B",
                What is the smallest planet in our solar system?, "A",
                Which city is known as the City of Love?, "A",
                What is the fastest bird in the world?, "A",
                Who discovered penicillin?, "B",
                What is the capital of Australia?, "C",
                Which planet is known as the Red Planet?, "A"
               
               
               ''')







questions = {
    "1. What is the tallest mountain in the world?": {"A": "Mount Everest", "B": "K2", "C": "Mount Kilimanjaro"},
    "2. Who wrote the novel 'To Kill a Mockingbird'?": {"A": "F. Scott Fitzgerald", "B": "Harper Lee", "C": "John Steinbeck"},
    "3. What is the chemical symbol for gold?": {"A": "Au", "B": "Ag", "C": "Fe"},
    "4. Who painted 'Starry Night'?": {"A": "Pablo Picasso", "B": "Vincent van Gogh", "C": "Claude Monet"},
    "5. What is the smallest planet in our solar system?": {"A": "Mercury", "B": "Pluto", "C": "Earth"},
    "6. Which city is known as the City of Love?": {"A": "Paris", "B": "Venice", "C": "Rome"},
    "7. What is the fastest bird in the world?": {"A": "Peregrine Falcon", "B": "Ostrich", "C": "Hummingbird"},
    "8. Who discovered penicillin?": {"A": "Marie Curie", "B": "Alexander Fleming", "C": "Louis Pasteur"},
    "9. What is the capital of Australia?": {"A": "Sydney", "B": "Melbourne", "C": "Canberra"},
    "10. Which planet is known as the Red Planet?": {"A": "Mars", "B": "Venus", "C": "Jupiter"}
}

answers = {
    "1": "A",
    "2": "B",
    "3": "A",
    "4": "B",
    "5": "A",
    "6": "A",
    "7": "A",
    "8": "B",
    "9": "C",
    "10": "A"
}
