import sqlite3
import json
import pandas as pd

# Load JSON data with UTF-8 encoding
with open('jsondata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert to DataFrame for easier handling
df = pd.json_normalize(data)

# Connect to SQLite database
conn = sqlite3.connect('dashboard.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS insights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        end_year TEXT,
        intensity INTEGER,
        sector TEXT,
        topic TEXT,
        insight TEXT,
        url TEXT,
        region TEXT,
        start_year TEXT,
        impact TEXT,
        added TEXT,
        published TEXT,
        country TEXT,
        relevance INTEGER,
        pestle TEXT,
        source TEXT,
        title TEXT,
        likelihood INTEGER
    )
''')

# Insert data into table
df.to_sql('insights', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()

print("Data loaded into SQLite database successfully!")