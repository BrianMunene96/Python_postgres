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

def get_students():

    con = get_connection()
    cur = con.cursor()
    cur.execute('SELECT name, city FROM students')
    rows = cur.fetchone()
    
    print(f'Name: {rows[0]}, city: {rows[1]}')
    cur.close()
    con.close()

get_students()