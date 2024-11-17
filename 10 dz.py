import sqlite3 as sql
connection = sql.connect('main.sl3')
cur = connection.cursor()
cur.execute('DROP TABLE students')
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT, 
    first_name TEXT,
    last_name TEXT,
    money INT
)
""")
cur.execute("INSERT INTO students VALUES(1, 'Raid', 'Bashirov', 10000)")
cur.execute("INSERT INTO students VALUES(2, 'Aidar', 'Aidarov', 100000)")
cur.execute("INSERT INTO students VALUES(3, 'Nurym', 'Durov', 10000000)")
cur.execute("INSERT INTO students VALUES(4, 'Ilon', 'Mask', 500)")
cur.execute("INSERT INTO students VALUES(5, 'qwe', 'rty', 990090)")


cur.execute("SELECT * FROM students")
res = cur.fetchall()
print(res)
connection.commit()
connection.close()
