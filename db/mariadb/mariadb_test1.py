import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="qwer1234",
    db="test",
    cursorclass=pymysql.cursors.DictCursor,
)
c = conn.cursor()

# sql = "create table if not exists stocks (data text,trans text,symbol text,qty real,price real)"
# c.execute(sql)
sql = """
        INSERT INTO STOCKS VALUES ('2020-07-08',
                                                'BUY',
                                                'RHAT',
                                                100,
                                                35.15)
    """
c.execute(sql)
conn.commit()
c.close()
conn.close()
