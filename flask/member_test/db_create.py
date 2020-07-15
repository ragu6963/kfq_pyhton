import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="qwer1234",
    db="test",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
try:
    # with conn.cursor() as cursor:
    #     sql = """
    #     drop table if exists users
    #     """
    #     cursor.execute(sql)
    #     conn.commit()

    # with conn.cursor() as cursor:
    #     sql = """
    #     create table users(
    #         userid varchar(20) primary key,
    #         userpw varchar(20) not null,
    #         username varchar(20) not null,
    #         userage integer,
    #         usermail varchar(20),
    #         useradd varchar(50),
    #         usergender varchar(20),
    #         usertel varchar(20)
    #         ) DEFAULT CHARSET=utf8
    #     """
    #     cursor.execute(sql)
    #     conn.commit()
    # with conn.cursor() as cursor:
    #     sql = """
    #     insert into users values
    #         ('gildong','1234','길동',33,'gildong@naver.com','경산','male','010-1234-5678')
    #     """
    #     cursor.execute(sql)
    #     conn.commit()

    with conn.cursor() as cursor:
        sql = """
            select * from users;
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()
