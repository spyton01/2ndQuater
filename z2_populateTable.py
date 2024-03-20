import sqlite3

# create empty database
connect = sqlite3.connect('QuestionsAnswer1.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS QA1
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO QA1 (id, questions, answers) VALUES
               (1, 'What is the tallest mountain in the world? A: Mount Everest B: K2 C: Mount Kilimanjaro', "A"),
               (2, 'Who wrote the novel "To Kill a Mockingbird"? A: F. Scott Fitzgerald B: Harper Lee C: John Steinbeck', "B"),
               (3, 'What is the chemical symbol for gold? A: Au B: Ag C: Fe', "A"),
               (4, 'Who painted Starry Night? A: Pablo Picasso, B: Vincent van Gogh, C: Claude Monet', "B"),
               (5, 'What is the smallest planet in our solar system? A: Mercury B: Pluto C: Earth', "A"),
               (6, 'Which city is known as the City of Love? A: Paris B: Venice C: Rome', "A"),
               (7, 'What is the fastest bird in the world? A: Peregrine Falcon B: Ostrich C: Hummingbird', "A"),
               (8, 'Who discovered penicillin? A: Marie Curie B: Alexander Fleming C: Louis Pasteur', "B"),
               (9, 'What is the capital of Australia? A: Sydney B: Melbourne C: Canberra', "C"),
               (10,'Which planet is known as the Red Planet? A: Mars B: Venus C: Jupiter', "A")
               ''')

cursor.execute('SELECT * FROM QA1')

print(cursor.fetchall())