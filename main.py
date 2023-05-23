from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Create a database and connection
connection = sqlite3.connect("Football")

# Create a table for storing data
connection.execute("CREATE TABLE IF NOT EXISTS Player (Jersey INTEGER PRIMARY KEY, Futboller STRING, Team STRING);")

# Add sample data
connection.execute("INSERT INTO Player (Jersey, Futboller, Team) VALUES (10, 'Michael Owen', 'Liverpool.')")

# Define routes

@app.get("/players")
async def get_players():
    cursor_object = connection.execute("SELECT * FROM Player")
    return cursor_object.fetchall()

@app.post("/players")
async def create_player(Jersey: int, Futboller: str, Team: str):
    new_player = (Jersey, Futboller, Team)
    connection.execute("INSERT INTO Player (Jersey, Futboller, Team) VALUES (?, ?, ?)", new_player)
    connection.commit()
    return {"message": "Player created successfully"}

@app.put("/players/{Jersey}")
async def update_player(Jersey: int, Team: str):
    connection.execute("UPDATE Player SET Team = ? WHERE Jersey = ?", (Team, Jersey))
    connection.commit()
    return {"message": "Player updated successfully"}

@app.delete("/players/{Jersey}")
async def delete_player(Jersey: int):
    connection.execute("DELETE FROM Player WHERE Jersey = ?", (Jersey,))
    connection.commit()
    return {"message": "Player deleted successfully"}

# Close the connection
connection.close()
