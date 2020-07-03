import json
import time
import random
import pickle

print("타자게임을 시작하겠습니다.")
word_list = "a a"
word_list = word_list.split(" ")
word_list = list(set(word_list))
player_list = {}
while True:
    print("1.타자게임 2.문제 불러오기 3.문제 저장하기 4.새문제 등록 5.등수 6.종료하기 ")
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
        # with open("./basic/quiz/word_list.pickle", 'wb') as f:
        #     pickle.dump(word_list, f)
        with open('./basic/quiz/data.json', 'wt') as f:
            json.dump(word_list, f, indent=4)
        
    elif menu == '4':
        word = input("등록할 문제를 입력하세요.\n>>>")
        word_list.append(word)
        word_list = list(set(word_list))
        print("문제 목록")
        print(word_list)
    elif menu == '5':
        player_lank = sorted(player_list.items(), key=lambda x: x[1])
        for i in range(0,len(player_lank)):
            name = player_lank[i][0]
            time = player_lank[i][1]
            print("{}등. {} - {:0.2f}초".format(i+1,name,time))
        
    elif menu == '6':
        break
    else:
        print("잘못된 입력입니다.")

# print(word_list)
