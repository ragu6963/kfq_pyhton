import cx_Oracle


class OracleDB:
    def connect(self):
        conn = cx_Oracle.connect(
            "hr/hr@localhost:1521/xe"
        )
        return conn

    def create_table(self):
        conn = self.connect()
        c = conn.cursor()
        sql = "CREATE SEQUENCE IF NOT EXISTS book_seq START WITH 1 INCREMENT BY 1"
        c.execute(sql)
        conn.commit()

        sql = """
                Create table books(
                                    book_id number not null,
                                    title VARCHAR2(50),
                                    published_date VARCHAR2(50),
                                    publisher VARCHAR2(50),
                                    pages number,
                                    recommend number,
                                    CONSTRAINT pk_book PRIMARY KEY(book_id))
                                    """
        c.execute(sql)
        conn.commit()
        conn.close()

    def insert_book(self, item):
        conn = self.connect()
        c = conn.cursor()
        sql = """insert into books values(book_seq.NEXTVAL,:1,:2,:3,:4,:5)"""
        c.execute(sql, item)
        conn.commit()
        conn.close()

    def select_book(self):
        conn = self.connect()
        c = conn.cursor()
        sql = """select * from books"""
        c.execute(sql)
        print(c.fetchall())
        conn.commit()
        conn.close()

    def select_book_id(self, id):
        conn = self.connect()
        c = conn.cursor()
        sql = """select * from books where book_id = :id"""
        c.execute(sql, id=id)
        print(c.fetchone())
        conn.commit()
        conn.close()


oracle = OracleDB()
# oracle.create_table()
item = (
    "생활코딩! 파이썬",
    "2020-07-13",
    "생활코딩",
    200,
    10,
)
# oracle.insert_book(item)
# oracle.select_book()
# oracle.select_book_id(25)
