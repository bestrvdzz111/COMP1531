import sqlite3

conn = sqlite3.connect('survey_system.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS choice_questions(question TEXT NOT NULL,choice1 TEXT,choice2 TEXT,choice3 TEXT)')

c.execute('CREATE TABLE IF NOT EXISTS text_questions(question TEXT)')


conn.commit()
conn.close()
