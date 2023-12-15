import pandas as pd
import pymysql

conn = pymysql.connect(
    host='127.0.0.1', 
    user='root', 
    password='12345', 
    db='algo_db',
)

cur = conn.cursor()

cur.execute('insert into orders values(10001, 10, 3.5)')
conn.commit()

cur.execute('select * from orders')
result = cur.fetchall()
for record in result:
    print(record)

conn.close()