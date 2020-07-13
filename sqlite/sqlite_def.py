import sqlite3


def create_conn():
    conn = sqlite3.connect("./kfq_python/sqlite/example.db")
    return conn


def create_table():
    conn = create_conn()
    c = conn.cursor()
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
    conn.commit()
    c.close()
    conn.close()


def insert_book(item):
    conn = create_conn()
    c = conn.cursor()
    sql = "INSERT INTO books values(?,?,?,?,?)"
    c.execute(sql, item)
    conn.commit()
    c.close()
    conn.close()


def insert_books(items):
    conn = create_conn()
    c = conn.cursor()
    sql = "INSERT INTO books values(?,?,?,?,?)"
    c.executemany(sql, items)
    conn.commit()
    c.close()
    conn.close()


def all_books():
    conn = create_conn()
    c = conn.cursor()
    sql = "Select * from books"
    c.execute(sql)
    books = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return books


def read_book_id(id):
    conn = create_conn()
    c = conn.cursor()
    sql = "Select * from books where rowid = %s" % id
    c.execute(sql)
    book = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return book


def read_book_title(title):
    conn = create_conn()
    c = conn.cursor()
    sql = "Select * from books where title LIKE ?"
    title = "%" + title + "%"
    c.execute(sql, (title,))
    book = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return book


if __name__ == "__main__":
    create_table()
    item = ["생활코딩! 파이썬", "2020-07-13", "생활코딩", 200, 10]

    # insert_book(item)
    items = [
        ["생활코딩! 자바", "2013-07-13", "생활코딩", 400, 10],
        ["생활코딩! 파이썬", "2020-07-13", "생활코딩", 200, 10],
    ]
    # insert_books(items)
    # all_books()
    # print(read_book_id(9))
    books = read_book_title("파이썬")
    for book in books:
        print(book)
