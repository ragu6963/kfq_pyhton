import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="qwer1234",
    db="test",
    cursorclass=pymysql.cursors.DictCursor,
)
c = conn.cursor()
t = ("RHAT",)

sql = """
        select * from stocks
        where symbol = %s
        """

c.execute(sql, t)
row = c.fetchall()
print(row)
conn.commit()
c.close()
conn.close()
