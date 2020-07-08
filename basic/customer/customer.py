import re
custlist = []

customer = {"name": "정우영", "gender": "f",
                    "email": "bhj123@naver.com", "birthyear": "1994"}
custlist.append(customer)
customer = {"name": "정우영1", "gender": "f",
            "email": "bhj123@naver.com", "birthyear": "1994"}
custlist.append(customer)
customer = {"name": "정우영2", "gender": "f",
            "email": "bhj123@naver.com", "birthyear": "1994"}
custlist.append(customer)

page = 2
index = 0
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

    choice = choice.upper()

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    if choice == "I":
        print("고객 정보 입력")
        customer = {"name": "", "gender": "",
                    "email": "", "birthyear": "", "page": ""}

        name = input("이름을 입력하세요.\n>>> ")
        customer['name'] = name
        while True:
            gender = input("성별을 입력하세요.\n>>> ")
            if gender in ["M", "m", "F", "f"]:
                customer["gender"] = gender.upper()
                break
            else:
                print("M m F f 로만 입력 가능합니다.")
        while True:
            e = re.compile('^[a-zA-z][0-9a-zA-Z]{4,}@[a-z]+.[a-z]{2,5}$')

            print("이메일 입력 규칙")
            print("첫글자 영문 소문자 혹은 대문자 및 숫자 영어 소문자 대문자로 이루어진 5글자 이상, @ 포함")
            email = input("이메일을 입력하세요.\n>>> ")
            check = 1
            for customer in custlist:
                if email == customer["email"]:
                    check = 0

            if check == 0:
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
                customer["birthyear"] = int(birthyear)
                break
            else:
                print("4자리 숫자 값을 입력해주세요.")
        customer["page"] = int(page) + 1
        print(customer)
        custlist.append(customer)
        page += 1

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == "C":
        print("현재 고객 정보 조회")

        if page == -1:
            print("고객이 존재하지 않습니다.")
            continue
        else:
            index = page
            customer = custlist[index]

            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == 'P':
        print("이전 고객 정보 조회")

        if page == -1:
            print("고객이 존재하지 않습니다.")
            continue

        if index == 0:
            pass

        else:
            index -= 1
        customer = custlist[index]
        print(customer)
        for c in customer:
            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page == -1:
            print("고객이 존재하지 않습니다.")
            continue

        if index == page:
            pass
        else:
            index += 1
        customer = custlist[index]
        print(customer)
        for c in customer:
            print("이름 : ", customer["name"])
            print("성별 : ", customer["gender"])
            print("출생년도 : ", customer["birthyear"])
            print("이메일 : ", customer["email"])

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == 'D':
        print("고객 정보 삭제")
        for customer in custlist:
            print("{} : {}".format(customer["name"],customer["email"]))

        email = input("삭제 할 고객의 이메일을 입력하세요.")
        delok = 0
        for i in range(0, len(custlist)):
            if email == custlist[i]["email"]:
                print("{} 님의 정보가 삭제되었습니다.".format(custlist[i]["name"]))
                delok = 1
                del custlist[i]
                break
        if delok == 1:
            page -= 1
            print("삭제가 완료되었습니다.")
        elif delok == 0:
            print("고객 정보가 존재하지 않습니다.")


#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == "U":
        print("고객 정보 수정")
        for customer in custlist:
            print("{} : {}".format(customer["name"],customer["email"]))

        email = input("수정 할 고객의 이메일을 입력하세요.")
        idx = -1
        for i in range(0, len(custlist)):
            if email == custlist[i]["email"]:
                idx = i
                break

        if idx == -1:
            print("고객 정보가 존재하지 않습니다.")

        else:
            customer = custlist[i]
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
                        e = re.compile('^[a-zA-z][0-9a-zA-Z]{4,}@[a-z]+.[a-z]{2,5}$')
                        print("이메일 입력 규칙")
                        print("첫글자 영문 소문자 혹은 대문자 및 숫자 영어 소문자 대문자로 이루어진 5글자 이상, @ 포함")
                        email = input("이메일을 입력하세요.\n>>> ")
                        check = 1
                        for customer in custlist:
                            if email == customer["email"]:
                                check = 0
                        if check == 0:
                            print("동일한 이메일이 있습니다.")
                            continue
                        if e.match(email) is not None:
                            customer["email"] = email
                            break
                        else:
                            print("이메일 입력 규칙이 틀렸습니다.")
                elif menu == '5':
                    break

                print("수정 후 정보")
                print(customer)

#TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:TODO:
    elif choice == "Q":
        print("프로그램 종료")
        break
