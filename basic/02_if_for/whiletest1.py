coffee = {}
coffee["아메리카노"] = 1500
coffee["아이스티"] = 2000
coffee["카페라떼"] = 2000
coffee["녹차라떼"] = 2500
coffee["쿠키프라페"] = 3000

prompt = '''
------------------------
    커피 자판기 메뉴    
------------------------
1. 커피 추가
2. 커피 삭제
3. 커피 메뉴판
4. 커피 구입
5. 종료
-----------------------
메뉴선택 >>>'''
while True:
    print(prompt)
    select = input()
    if select == '1':
        print("커피메뉴를 추가합니다.")
        name = input("메뉴명>>> ")
        price = int(input("가격>>> "))
        coffee[name] = price
        print(coffee)
        print("{} 메뉴는 {:,}원 입니다.".format(name, price))

    elif select == '2':
        print("커피메뉴를 삭제합니다.")
        print(coffee)
        name = input("삭제할 커피 메뉴명>>> ")
        coffee.pop(name)
        print(coffee)

    elif select == '3':
        for k, v in coffee.items():
            print("메뉴 : {} , 가격 : {:,} ".format(k, v))

    elif select == '4':
        print("커피 메뉴를 선택해주세요.")
        print(coffee)
        name = input("추출할 커피 메뉴명>>> ")

        if coffee.get(name) is not None:
            money = int(coffee[name])
            print("{}의 가격은 {:,}원 입니다.".format(name, money))
            print("돈을 넣어주세요")
            inputmoney = int(input("금액>>> "))
            if inputmoney >= money:
                print("{}가 나옵니다.".format(name))
                print("거스름돈 {:,}원이 나옵니다.".format(inputmoney-money))
            else:
                print("{:,}원이 부족합니다".format(money-inputmoney))
        else:
            print("{}은 존재하지 않는 메뉴입니다.".format(name))

    elif select == '5':
        print("프로그램 종료")
        break
