import pymysql


class MariaDB:
    def __connect(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qwer1234",
            db="test",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.c = self.conn.cursor()

    def __unconnect(self):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.__connect()
        sql = """create table if not exists books 
        (book_id integer Not null Auto_increment primary key, 
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer)DEFAULT CHARSET=utf8;
        """
        self.c.execute(sql)
        self.__unconnect()

    def insert_book(self, item):
        self.__connect()
        sql = "INSERT INTO books (title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)"
        self.c.execute(sql, item)
        self.__unconnect()

    def insert_books(self, items):
        self.__connect()
        sql = "INSERT INTO books  (title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)"
        self.c.executemany(sql, items)
        self.__unconnect()

    def select_all(self):
        self.__connect()
        sql = "Select * from books"
        self.c.execute(sql)
        books = self.c.fetchall()
        self.__unconnect()
        return books

    def select_book_id(self, book_id):
        self.__connect()
        sql = "Select * from books where book_id = %s"
        self.c.execute(sql, book_id)
        book = self.c.fetchone()
        self.__unconnect()
        return book

    def select_book_condition(
        self, condition, value
    ):
        self.__connect()
        sql = (
            "Select * from books where "
            + condition
            + " LIKE %s"
        )
        value = "%" + value + "%"
        self.c.execute(sql, value)
        books = self.c.fetchall()
        self.__unconnect()
        return books

    def update_book_title(self, title, book_id):
        self.__connect()
        sql = "Update books set title =  %s  Where book_id = %s"
        self.c.execute(sql, (title, book_id))
        self.__unconnect()

    def delete_book_id(self, book_id):
        self.__connect()
        sql = (
            "Delete from books where book_id = %s"
        )
        self.c.execute(sql, book_id)
        self.__unconnect()


maria = MariaDB()
# maria.create_table()
# -------------------------------- INSERT
# item = ["생활코딩! HTML+CSS", "2020-07-13", "생활코딩", 200, 10]
# maria.insert_book(item)

# -------------------------------- SELECT ALL
# books = maria.select_all()
# print(books)

# -------------------------------- SELECT ID
# book_id = maria.select_book_id(3)
# print(book_id)

# -------------------------------- SELECT CONDITION
# books = maria.select_book_condition("title", "h")
# print(books)

# -------------------------------- UPDATE TITLE
# maria.update_book_title("생활코딩! 자바", 1)
# books = maria.select_all()
# print(books)

# -------------------------------- DELETE ID
# maria.delete_book_id(2)
# books = maria.select_all()
# print(books)

