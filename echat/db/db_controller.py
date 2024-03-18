import sqlite3

conn = sqlite3.connect('echat.db')
cursor = conn.cursor()

def insert_user(username, password_hash, access_level=0):
  try:
    
    cursor.execute("INSERT INTO users (username, password_hash, access_level) VALUES (?, ?, ?)",
                   (username, password_hash, access_level))
    conn.commit()
    return True
  except sqlite3.Error as e:
    print("Error:", e)
    return False

def fetch_user(username):
  try:
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    return user_data
  except sqlite3.Error as e:
    print("Error:", e)
    return None
  
def fetch_all_usernames():
  try:
    cursor.execute("SELECT username FROM users")
    usernames = [username[0] for username in cursor.fetchall()]
    return usernames 
  except sqlite3.Error as e:
    print("Error:", e)
    return None


#only executed after fetch_user
def fetch_password_hash(username):
  user_data = fetch_user(username)
  if user_data:
    return user_data[1]
  else:
    return None  



def db_first_run():
    
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
  if cursor.fetchone() is None:
     print("DB First Run: Configuring database")
     cursor.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password_hash TEXT, access_level INTEGER)")
     conn.commit()
     print("SUCCESS | Database is now awake!")
  else:
    print("Database was already configured")
