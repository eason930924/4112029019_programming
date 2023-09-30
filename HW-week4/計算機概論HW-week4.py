import sqlite3
conn=sqlite3.connect('BBQ.db')
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat(
        id INTERGER PRIMARY KEY,
        name TEXT,
        price INTERGER,
        quantity INTERGER
    )''')

cursor.execute("INSERT INTO meat(id,name,price,quantity) VALUES(1,'chicken',30,5)")
cursor.execute("INSERT INTO meat(id,name,price,quantity) VALUES(2,'beaf',55,10)")
cursor.execute("INSERT INTO meat(id,name,price,quantity) VALUES(3,'pork',40,15)")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("BBQ列表:")
for MEAT in meat:
    print(MEAT)

cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("BBQ列表:")
for MEAT in meat:
    print(MEAT)

cursor.execute("DELETE FROM meat WHERE price = 40")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("BBQ列表:")
for MEAT in meat:
    print(MEAT)