import time
import random
print("타자게임을 시작하겠습니다.")
word_list = "at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed"
word_list = word_list.split(" ")
word_list = list(set(word_list))
print(word_list)

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
