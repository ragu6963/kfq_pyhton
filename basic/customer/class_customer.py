import re
import sys


class Customer:
    emaillist = ['hong1@gmail.com', 'kims1@gmail.com',
                 'park1@gmail.com', 'kim00@gmail.com', ]
    custlist = [{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': 2000},
                {'name': '김길동', 'gender': 'M',
                    'email': 'kims1@gmail.com', 'birthyear': 2010},
                {'name': '박나리', 'gender': 'F',
                    'email': 'park1@gmail.com', 'birthyear': 1999},
                {'name': '김철수', 'gender': 'M', 'email': 'kim00@gmail.com', 'birthyear': 1988}]
    page = 3
    index = 0

    def __init__(self):
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
            ''').upper()

            self.exe(choice)

    def exe(self, choice):
        if choice == 'I':
            self.insertData()

        elif choice == 'C':
            self.curSearch()

        elif choice == 'P':
            self.preSearch()

        elif choice == 'N':
            self.nextSearch()

        elif choice == 'U':
            self.updateData()

        elif choice == 'D':
            self.deleteData()

        elif choice == 'Q':
            sys.exit()

    def insertData(self):
        print("고객 정보 입력")

        name = input("이름을 입력하세요.\n>>> ")

        while True:
                gender = input("성별을 입력하세요.\n>>> ")
                if gender in ["M", "m", "F", "f"]:
                    gender = gender.upper()
                    customer["gender"] = gender
                    break
                else:
                    print("M m F f 로만 입력 가능합니다.")

        while True:
            e = re.compile('^[a-zA-z][0-9a-zA-Z]{4,}@[a-z]+.[a-z]{2,5}$')

            print("이메일 입력 규칙")
            print("첫글자 영문 소문자 혹은 대문자 및 숫자 영어 소문자 대문자로 이루어진 5글자 이상, @ 포함")
            email = input("이메일을 입력하세요.\n>>> ")
            if email in self.emaillist:
                print("동일한 이메일이 있습니다.")
                continue
            if e.match(email) is not None:
                customer["email"] = email
                break
            else:
                print("이메일 입력 규칙이 틀렸습니다.")

        while True:
            birthyear = input("출생년도를 입력하세요.\n>>> ")
            if len(birthyear) == 4 and birthyear.isdecimal():
                birthyear = int(birthyear)
                customer["birthyear"] = birthyear
                break
            else:
                print("4자리 숫자 값을 입력해주세요.")

        customer = {"name": name, "gender": gender,
                    "email": email, "birthyear": birthyear}

        print(customer)
        self.emaillist.append(email)
        self.custlist.append(customer)
        self.page += 1

    def curSearch(self):
        if self.page == -1:
            print("고객이 존재하지 않습니다.")
        else:
            index = self.page
            customer = self.custlist[index]
            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

    def preSearch(self):
        print("이전 고객 정보 조회")
        if self.page == -1:
            print("고객이 존재하지 않습니다.")
        else:
            if self.index == 0:
                pass
            else:
                self.index -= 1

            customer = self.custlist[self.index]
            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

    def nextSearch(self):
        print("다음 고객 정보 조회")
        if self.page == -1:
            print("고객이 존재하지 않습니다.")
        else:
            if self.index == self.page:
                pass
            else:
                self.index += 1
            customer = self.custlist[self.index]
            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

    def deleteData(self):
        print("고객 정보 삭제")
        for customer in self.custlist:
            print("{} : {}".format(customer["name"], customer["email"]))

        email = input("삭제 할 고객의 이메일을 입력하세요.")
        if email in self.emaillist:
            print("{} 님의 정보가 삭제되었습니다.".format(self.custlist[i]["name"]))
            index = self.emaillist.index(email)
            del self.custlist[index]
            del self.emaillist[index]
            self.page -= 1
            print("삭제가 완료되었습니다.")

        else:
            print("고객 정보가 존재하지 않습니다.")

    def updateData(self):
        print("고객 정보 수정")
        for customer in self.custlist:
            print("{} : {}".format(customer["name"], customer["email"]))

        email = input("수정 할 고객의 이메일을 입력하세요.")
        if email in self.emaillist:
            index = self.emaillist.index(email)
            customer = self.custlist[index]
            while True:
                print("수정을 원하는 정보를 선택하세요.")
                menu = input("1. 이름 2. 성별 3. 출생년도 4. 이메일 5. 돌아가기")
                if menu == '1':
                    name = input("이름을 입력하세요.\n>>> ")
                    customer['name'] = name

                elif menu == '2':
                    while True:
                        gender = input("성별을 입력하세요.\n>>> ")
                        if gender in ["M", "m", "F", "f"]:
                            customer["gender"] = gender.upper()
                            break
                        else:
                            print("M m F f 로만 입력 가능합니다.")

                elif menu == '3':
                    while True:
                        birthyear = input("출생년도를 입력하세요.\n>>> ")
                        if len(birthyear) == 4 and birthyear.isdecimal():
                            customer["birthyear"] = int(birthyear)
                            break
                        else:
                            print("4자리 숫자 값을 입력해주세요.")

                elif menu == '4':
                    while True:
                        e = re.compile(
                            '^[a-zA-z][0-9a-zA-Z]{4,}@[a-z]+.[a-z]{2,5}$')
                        print("이메일 입력 규칙")
                        print("첫글자 영문 소문자 혹은 대문자 및 숫자 영어 소문자 대문자로 이루어진 5글자 이상, @ 포함")
                        email = input("이메일을 입력하세요.\n>>> ")
                        check = 1
                        if email in self.emaillist:
                            print("동일한 이메일이 있습니다.")
                            continue
                        if e.match(email) is not None:
                            customer["email"] = email
                            self.emaillist[index] = email
                            break
                        else:
                            print("이메일 입력 규칙이 틀렸습니다.")
                elif menu == '5':
                    break

                print("수정 후 정보")
                print(customer)

Customer()
