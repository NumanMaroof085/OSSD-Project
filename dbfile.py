import sqlite3

DB_NAME = "Notes.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table(catagory):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {catagory} (
            title TEXT NOT NULL,
            text TEXT
        )
    ''')
    conn.commit()
def create_table2(catagory):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {catagory} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Pass TEXT
        )
    ''')
    conn.commit()
def insert_data(catagory,title,text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {catagory} (title,text)
        VALUES (?,?)
    ''', (title,text,))
    conn.commit()

def read_data(catagory, title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {catagory} WHERE title = ?", (title,))
    return cursor.fetchall()

def fetch_all_notes(choice):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    notes = []
    # Define tables you want to skip
    skip_tables = {"Password","sqlite_sequence"}  
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]

        if table_name in skip_tables:
            continue  # Skip this table
        if choice=="categories":
            notes.append(table_name)
            continue
        try:
            cursor.execute(f'SELECT title FROM "{table_name}"')
        except sqlite3.OperationalError as e:
            print(f"Error in table '{table_name}': {e}")
            continue
        rows = cursor.fetchall()
        if( choice == "notes"):
            for row in rows:
                notes.append({
                    "title": row[0],
                    "category": table_name
                })
    conn.close()
    return notes


def update_data(catagory,title, text):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute(f'''
            UPDATE {catagory}
            SET text = ?
            WHERE title = ?
        ''',(text,title,))
    conn.commit()

def delete_data(catagory, title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'''
        DELETE FROM {catagory} 
        WHERE title= ?
    ''',(title,))
    conn.commit()

def change_pass(new_pass):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Password
        SET Pass = ?
        where id = 1
    ''',(new_pass,))
    conn.commit()

def read_pass(key):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Password WHERE id = ?", (key,))
    return cursor.fetchall()