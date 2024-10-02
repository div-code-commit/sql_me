import sqlite3

def create_db():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Create a table for recipes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
