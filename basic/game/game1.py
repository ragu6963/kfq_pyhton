# 1~50 사이의 숫자 중 임의의 숫자를 선택해서 덧셈 문제를 내면 맞추는 게임.

import random
cnt = 0
for i in range(0, 3):
    number1 = int(random.randint(1, 50))
    number2 = int(random.randint(1, 50))
    question = "{} + {}".format(number1, number2)
    answer = eval(question)
    print(answer)
    inputanswer = int(input(question+" = ?\n >>>"))

    if(answer == inputanswer):
        print("정답!")
        cnt += 1
    else:
        print("오답!")

print("{}개 맞음".format(cnt))
