import sqlite3
import csv

# CREATE TABLE
input_file = "kfq_python/sqlite/input.csv"

conn = sqlite3.connect("kfq_python/sqlite/suppliers.db")

c = conn.cursor()

sql = """
        create table if not exists suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            part_number varchar(20),
            cost float,
            purchase_date date
        )
    """
c.execute(sql)
conn.commit()

# csv -> sqllite
file_reader = csv.reader(open(input_file, "r"), delimiter=",")
header = next(file_reader, None)
print(header)
data = []
for row in file_reader:
    print(type(row))
    data.append(row)
print(data)
print(type(data))
sql = "insert into suppliers values(?,?,?,?,?)"
c.executemany(sql, data)
conn.commit()

# 데이터 삭제
sql = "delete from suppliers"
c.execute(sql)
conn.commit()

c.close()
conn.close()
