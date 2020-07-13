import random
import time
cnt = 0
input("enter를 누르면 20초를 셉니다.")
start = time.time()
for i in range(0,3):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    oper_list = ["+", "-", "//", "*"]

    oper = random.choice(oper_list)

    expression = "{} {} {}".format(a,oper,b)

    answer = eval(expression)
    
    inputanswer = int(input(expression+" = ?\n>>> "))
    if(answer == inputanswer):
        cnt+=1
        print('정답')
    else:
        print("오답")
        
end = time.time()
print("{}개 맞췄으며 {}초 걸렸습니다".format(cnt,end-start))
