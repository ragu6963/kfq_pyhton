import sqlite3

conn = sqlite3.connect("./kfq_python/sqlite/example.db")

c = conn.cursor()

# Select문 1
# symbol = "RHAT"
# c.execute(
#     """
#         select * from stocks
#         where symbol = '%s'
#     """
#     % symbol
# )

# print(c.fetchone())

# Select문 2
# t = ("RHAT",)
# sql = "select * from stocks where symbol =?"
# c.execute(sql, t)
# print(c.fetchone())

# 다중 Insert
# items = [
#     ("2020-07-09", "BUY", "IBM", 1000, 45.00),
#     ("2020-07-10", "SELL", "MSFT", 500, 72.00),
# ]
# sql = "insert into stocks values(?,?,?,?,?)"
# c.executemany(sql, items)

# SELECT * ORDER BY
sql = "select * from stocks order by price"
c.execute(sql)
rows = c.fetchall()

for row in rows:
    # print(row)
    # print(type(row))
    print(row[0])

print(type(rows))
conn.commit()
c.close()
conn.close()

