import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

# Connecting to the PostgreSQL database
def get_connection():
    con = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return con

# Cursor to connect to the database and execute SQL commands
con = get_connection()
cur = con.cursor()

#Cursor contains an execute command method -> multiple line sripts
cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            city VARCHAR(80),
            score NUMERIC(4, 2)
 )           
''')

# Save changes to the database
con.commit()

# Close the cursor 
cur.close()

# Close the connection to the database
con.close()