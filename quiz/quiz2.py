import sys
stulist = []
numlist = []

def exe(choice):
    global stulist,numlist
    if choice == "1":
        stulist,numlist = insert(stulist,numlist)
    elif choice == "2":
        stulist,numlist = update(stulist,numlist)
    elif choice == "3":
        stulist,numlist = delete(stulist,numlist)
    elif choice == "4":
        read(stulist,numlist)
    elif choice == "5":
        sys.exit()


def insert(stulist,numlist):
    print("학생 정보 입력")
    student = {"name": "", "number": "",
                "major": "", "phonenumber": "", "address": ""}
    while True:
        number = input("학번을 입력하세요.\n>>> ")
        if number in numlist:
            print("이미 존재하는 학번입니다.")
            continue

        if number.isdecimal():
            student['number'] = number
            break
        else:
            print("숫자만 입력하세요.")

    name = input("이름을 입력하세요.\n>>> ")
    student['name'] = name
    major = input("학과를 입력하세요.\n>>> ")
    student['major'] = major

    while True:
        phonenumber = input("전화번로를 입력하세요.\n>>> ")
        if phonenumber.isdecimal() and (len(phonenumber) == 11 or len(phonenumber) ==10): 
            student['phonenumber'] = phonenumber
            break
        else:
            print("11자리 또는 10자리 숫자만 입력하세요.")

    address = input("주소를 입력하세요.\n>>> ")
    student['address'] = address

    stulist.append(student)
    numlist.append(number)
    print("입력 정보 확인")
    print(student)
    return stulist,numlist

def update(stulist,numlist):
    print("학생 정보 수정")
    if len(stulist) != 0:
        for student in stulist:
            print("{} : {}".format(student["name"],student["number"]))

        number = input("수정 할 학생의 학번을 입력하세요.\n>>> ")
        if number in numlist:
            index = numlist.index(number)
            student = stulist[index]
            while True:
                print("수정을 원하는 정보를 선택하세요.")
                menu = input("1. 이름 2. 학번 3. 학과 4. 전화번호 5. 주소 6. 돌아가기\n>>> ")
                if menu == '1':
                    name = input("이름을 입력하세요.\n>>> ")
                    student['name'] = name

                elif menu == '2':
                    while True:
                        number = input("학번을 입력하세요.\n>>> ")
                        if number in numlist:
                            print("이미 존재하는 학번입니다.")
                            continue

                        if number.isdecimal():
                            student['number'] = number
                            break
                        else:
                            print("숫자만 입력하세요.")

                elif menu == '3':
                    major = input("학과를 입력하세요.\n>>> ")
                    student['major'] = major

                elif menu == '4':
                    while True:
                        phonenumber = input("전화번로를 입력하세요.\n>>> ")
                        if phonenumber.isdecimal() and (len(phonenumber) == 11 or len(phonenumber) ==10):
                            student['phonenumber'] = phonenumber
                            break
                        else:
                            print("11자리 또는 10자리 숫자만 입력하세요.")

                elif menu == '5':
                    address = input("주소를 입력하세요.\n>>> ")
                    student['address'] = address

                elif menu == '6':
                    stulist[index] = student
                    numlist[index] = number
                    return stulist,numlist
    else:
        print("등록 된 학생이 없습니다")


def delete(stulist,numlist):
    print("학생 정보 삭제")
    if len(stulist) != 0:
        for student in stulist:
            print("{} : {}".format(student["name"],student["number"]))

        number = input("삭제 할 학생의 학번을 입력하세요.\n>>> ")
        if number in numlist:
            index = numlist.index(number)
            print("{} 님의 정보가 삭제되었습니다.".format(stulist[index]["name"]))
            del stulist[index]
            del numlist[index]
            print("삭제가 완료되었습니다.")
            return stulist,numlist
        else:
            print("학생 정보가 존재하지 않습니다.")
    else:
        print("등록 된 학생이 없습니다")


def read(stulist,numlist):
    print("학생 정보")
    if len(stulist) == 0:
        print("등록 된 학생이 없습니다")
    else:
        for student in stulist:
            print(student)

while True:
    choice = input('''
    다음 중에서 하실 일을 골라주세요 :
    1. 학생 정보 입력
    2. 학생 정보 수정
    3. 학생 정보 삭제
    4. 학생 정보 열람
    5. 종료
    ''')
    exe(choice)