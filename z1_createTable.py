import sqlite3

# create empty database
connect = sqlite3.connect('QuestionsAnswer1.db')
cursor = connect.cursor()

cursor.execute('SELECT * FROM QuestionsAnswer1')

cursor.execute('''CREATE TABLE IF NOT EXISTS QuestionsAnswer1
               (id integer, questions text, answers text)''')

print(cursor.fetchall())