import psycopg2
from mydb import get_connection

# Connecting to the PostgreSQL database
def insert_student(name, city, score):
    con = get_connection()
    cur = con.cursor()

    cur.execute('INSERT INTO students (name, city, score) VALUES (%s, %s, %s)', 
                (name, city, score)
    )

    con.commit()
    cur.close()
    con.close()

    print(f'Student {name} added successfully!')



