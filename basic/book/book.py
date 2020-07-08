# TODO: 책 등록 / 책 수정 / 책 삭제 / 책 판매


import re
booklist = []

page = -1
index = 0
while True:
    choice = input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 책 등록
    Q - 프로그램 종료
    ''')