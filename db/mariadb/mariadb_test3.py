import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="qwer1234",
    db="test",
    cursorclass=pymysql.cursors.DictCursor,
)
c = conn.cursor()
items = [
    ("2020-07-09", "BUY", "IBM", 1000, 45.00),
    ("2020-07-10", "SELL", "MSFT", 500, 72.00),
]

sql = "insert into stocks values(%s,%s,%s,%s,%s)"
# c.executemany(sql, items)
conn.commit()

sql = """
        select * from stocks 
        """
c.execute(sql)
row = c.fetchall()
for r in row:
    print(r)

c.close()
conn.close()
