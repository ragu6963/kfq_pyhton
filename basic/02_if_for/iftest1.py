# 숫자를 입력받아서 짝수인지 홀수인지 판별
number = input("숫자를 입력하세요\n> ")

if number.isdecimal():
    if int(number) == 0:
        print("{}는 0입니다".format(int(number)))

    elif int(number) % 2 == 0:
        print("{}는 짝수입니다".format(int(number)))

    elif int(number) % 2 != 0:
        print("{}는 홀수입니다".format(int(number)))

else:
    print("{}는 숫자가 아닙니다.".format(number))
