import json
import time
import random
import pickle

print("타자게임을 시작하겠습니다.")
word_list = "a a"
word_list = word_list.split(" ")
word_list = list(set(word_list))
player_list = {}

try:
    with open('./basic/quiz/rank.json', 'rt') as f:
        player_list = json.load(f)
except:
    with open('./basic/quiz/rank.json', 'wt') as f:
        json.dump(player_list, f, indent=4)

while True:
    print("1.타자게임 2.문제 불러오기 3.문제 저장하기 4.문제 등록 수정 삭제 5.등수 6.종료하기 ")
    menu = input("메뉴를 선택하세요.\n>>> ")
    if menu == '1':
        input("enter를 누르면 시간측정을 시작합니다.")
        start = time.time()
        for i in range(0, 5):
            word = random.choice(word_list)
            while True:
                input_word = input(word+"\n입력 >")
                if word == input_word:
                    print("정답")
                    break
                else:
                    print("오답")
        end = time.time()
        print("걸린시간 {}".format(end-start))
        player = input("플레이어 이름을 입력하세요.\n>>> ")
        player_list[player] = end-start

    elif menu == '2':
        # with open("./basic/quiz/word_list.pickle", "rb") as f:
        #     word_list = pickle.load(f)
        with open('./basic/quiz/data.json', 'rt') as f:
            word_list = json.load(f)

        word_list = list(set(word_list))
        print("문제 목록")
        print(word_list)

    elif menu == '3':
        # with open("./basic/quiz/word_list.pickle", 'wb') as  f:
        #     pickle.dump(word_list, f)
        with open('./basic/quiz/data.json', 'wt') as f:
            json.dump(word_list, f, indent=4)

    elif menu == '4':
        while True:
            print("1.문제 등록 2.문제 수정 3.문제 삭제 4.돌아가기")
            select = input("메뉴를 선택하세요.\n>>> ")
            if select == '1':
                create_word = input("등록할 단어를 입력하세요.\n>>>")
                if create_word in word_list:
                    print("이미 존재하는 단어입니다.")
                else:
                    word_list.append(create_word)
                    print("단어가 추가되었습니다.")
            elif select == '2':
                print("문제 목록")
                print(word_list)
                update_word = input("수정 할 단어를 입력하세요.\n>>>")
                if update_word in word_list:
                    index = word_list.index(update_word)
                    change_word = input("어떤 단어로 수정할지 입력하세요.\n>>>")
                    word_list[index] = change_word
                    print("수정이 완료되었습니다.,")
                else:
                    print("존재하지 않는 단어입니다.")
            elif select == '3':
                print("문제 목록")
                print(word_list)
                delete_word = input("삭제 할 단어를 입력하세요.\n>>>")
                if delete_word in word_list:
                    word_list.remove(delete_word)
                    print("삭제가 완료되었습니다.")
                else:
                    print("존재하지 않는 단어입니다.")
            elif select == '4':
                break
            else:
                print("잘못된 입력입니다.")

    elif menu == '5':
        player_lank = sorted(player_list.items(), key=lambda x: x[1])
        for i in range(0, len(player_lank)):
            name = player_lank[i][0]
            record = player_lank[i][1]
            print("{}등. {} - {:0.2f}초".format(i+1, name, record))

    elif menu == '6': 
        break
    else:
        print("잘못된 입력입니다.")

with open('./basic/quiz/rank.json', 'wt') as f:
    json.dump(player_list, f, indent=4)