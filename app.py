 from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "Football.db"  # Changed the database name to "Football.db"

# Function to get the database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM Player")
    players = cursor.fetchall()
    conn.close()
    return render_template("index.html", players=players)

# Update route
@app.route("/update")
def update():
    conn = get_db_connection()
    conn.execute("UPDATE Player SET Team = 'I WRITE WHAT I LIKE' WHERE Jersey = 1")
    conn.commit()
    conn.close()
    return "Player updated successfully!"

# Delete route
@app.route("/delete")
def delete():
    conn = get_db_connection()
    conn.execute("DELETE from Player WHERE Jersey = 1")
    conn.commit()
    conn.close()
    return "Player deleted successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)