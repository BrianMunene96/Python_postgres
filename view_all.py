from mydb import get_connection

def get_all_students():

    con = get_connection()
    cur = con.cursor()
    cur.execute('SELECT name, city FROM students')
    rows = cur.fetchall()

    for row in rows:
        print(f'Name: {row[0]}, city: {row[1]}')
    
    cur.close()
    con.close()

get_all_students()

