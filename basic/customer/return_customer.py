import re
custlist = []
page = -1


def exe(choice):
    choice = choice.upper()
    if choice == 'I':
        insertData()

    elif choice == 'C':
        curSearch()

    elif choice == 'P':
        preSearch()

    elif choice == 'N':
        nextSearch()

    elif choice == 'U':
        updateData()

    elif choice == 'D':
        deleteData()

    elif choice == 'Q':
        quit()


def insertData():
    pass


def curSearch():
    pass


def preSearch():
    pass


def nextSearch():
    pass


def deleteData():
    pass


def updateData():
    pass


while True:
    choice = input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')

    exe(choice)
