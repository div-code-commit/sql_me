from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
def connect_db():
    return sqlite3.connect('recipes.db')

# Route for the home page
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)

# Route to display form for adding a new recipe
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO recipes (name, ingredients, instructions) VALUES (?, ?, ?)",
                       (name, ingredients, instructions))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add.html')

# Route to delete a recipe
@app.route('/delete/<int:id>')
def delete_recipe(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

