
import sqlite3

conn = sqlite3.connect("food_calories.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS foods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT UNIQUE,
    calories INTEGER
)
''')

sample_data = [
    ("Apple", 52),
    ("Banana", 89),
    ("Rice", 130),
    ("Bread", 265),
    ("Egg", 155),
    ("Milk", 42)
]

for food in sample_data:
    try:
        cursor.execute("INSERT INTO foods (food_name, calories) VALUES (?, ?)", food)
    except:
        pass

conn.commit()
conn.close()
print("Database Ready")
