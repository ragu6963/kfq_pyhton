import sqlite3


class SqlLite:
    def __create_conn(self):
        self.__conn = sqlite3.connect("./kfq_python/sqlite/example.db")

    def create_table(self):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = """
                create table if not exists books(
                    title text,
                    published_data text,
                    publisher text,
                    pages integer,
                    recommend integer
                )
            """
        c.execute(sql)
        self.__conn.commit()
        c.close()
        self.__conn.close()

    def insert_book(self, item):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = "INSERT INTO books values(?,?,?,?,?)"
        c.execute(sql, item)
        self.__conn.commit()
        c.close()
        self.__conn.close()

    def insert_books(self, items):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = "INSERT INTO books values(?,?,?,?,?)"
        c.executemany(sql, items)
        self.__conn.commit()
        c.close()
        self.__conn.close()

    def all_books(self):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = "Select * from books"
        c.execute(sql)
        books = c.fetchall()
        self.__conn.commit()
        c.close()
        self.__conn.close()
        return books

    def read_book_id(self, id):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = "Select * from books where rowid = %s" % id
        c.execute(sql)
        book = c.fetchall()
        self.__conn.commit()
        c.close()
        self.__conn.close()
        return book

    def read_book_title(self, title):
        self.__create_conn()
        c = self.__conn.cursor()
        sql = "Select * from books where title LIKE ?"
        title = "%" + title + "%"
        c.execute(sql, (title,))
        book = c.fetchall()
        self.__conn.commit()
        c.close()
        self.__conn.close()
        return book


sql = SqlLite()
sql.create_table()

item = ["생활코딩! 파이썬", "2020-07-13", "생활코딩", 200, 10]
# sql.insert_book(item)

items = [
    ["생활코딩! 자바", "2013-07-13", "생활코딩", 400, 10],
    ["생활코딩! HTML&CSS3", "2020-07-13", "생활코딩", 200, 10],
]
# sql.insert_books(items)

books = sql.all_books()
# for book in books:
#     print(book)

# print(sql.read_book_id(1))
books = sql.read_book_title("생활코딩")
for book in books:
    print(book)
