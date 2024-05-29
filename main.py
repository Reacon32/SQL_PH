import sqlite3

conn = sqlite3.connect('animals.dp')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS animals (
    id INTEGER PRIMARY KEY,
    name TEXT NUT NULL,
    limbs INTEGER
)
''')

cursor.execute('''
INSERT INTO animals (name, limbs)
VALUES ('Dog', 4), ('Spider', 8), ('Parrot', 4)
''')

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()