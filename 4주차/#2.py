#Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.
#글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.
#변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.

def count_word(text, word):

    text_save = open("text.txt", "w", encoding="UTF8")

    text_save.write(text)

    text_save.close()

    

    count = 0 

    word_length = len(word) 

    word_save = "" 

    

    f_1 = open("text.txt") 

    for line in f_1: 

        if word in line:

            for s in line:

                word_save = word_save + s 

                if word_save == word: 

                    count += 1 # count +1

                if len(word_save) == len(word): 

                    word_save = word_save[1:]

    print(count) 
