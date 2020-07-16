import sqlite3
conn = sqlite3.connect("./kfq_python/sqlite/example.db")

cur = conn.cursor()

cur.execute('''
            CREATE TABLE if not exists STOCKS(data text,
                                trans text,
                                symbol text,
                                qry real,
                                price real)
             ''')

cur.execute('''
            INSERT INTO STOCKS VALUES ('2020-07-08',
                                        'BUY',
                                        'RHAT',
                                        100,
                                        35.15)
            ''')
conn.commit()
conn.close()