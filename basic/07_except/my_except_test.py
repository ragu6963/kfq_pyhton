class MyError(Exception):
    def __init__(self):
        print("바보 ㄴㄴ")
    def __str__(self):
        return "바보 하지마"

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("qq")
    say_nick("바보")
except MyError as err:
    print(err)