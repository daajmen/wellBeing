import sqlite3
from datetime import datetime
import os

# Funktion för att ansluta till databasen och skapa tabellen om den inte finns
def init_db():
    # Skapa katalogen om den inte finns
    if not os.path.exists('db'):
        os.makedirs('db')

    # Anslut till databasen
    conn = sqlite3.connect('db/events.db')
    cursor = conn.cursor()
    
    # Skapa tabellen om den inte redan finns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT,
            action TEXT,
            user_id TEXT,
            time_fired TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Funktion för att lagra händelsen i databasen
def insert_event(event_type, action, user_id, time_fired):
    conn = sqlite3.connect('db/events.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO events (event_type, action, user_id, time_fired) 
        VALUES (?, ?, ?, ?)
    ''', (event_type, action, user_id, time_fired))
    
    conn.commit()
    conn.close()

# Exempel på funktion för att hämta alla händelser
def fetch_events():
    conn = sqlite3.connect('db/events.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM events')
    rows = cursor.fetchall()
    
    conn.close()
    return rows
