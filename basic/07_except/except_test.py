# f=open("text.txt",'r')


try:
    4/0
    li= [2,3]
    li[4]
except IndexError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("finally")