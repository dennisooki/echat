#create a function to delete everything from the database
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def delete_everything():
    cursor.execute("DELETE FROM users")
    conn.commit()