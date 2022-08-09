#Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.

#주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
#뒷자리는 1,3 은 남자 2,4는 여자
#00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
#뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

#주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.

def check_id(id_number):
    while True:
        if len(id_number) != 14 or id_number.find("-") == -1:
            print("잘못된 번호입니다.")
            break
        if int(id_number[:2]) <=21:
            q = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
            if q == "o":
                if id_number[7] not in ["3" ,"4"]:
                    print("잘못된 번호입니다.")
                else:
                    if id_number[7] == "3":
                        gender = "남자"
                    else:
                        gender = "여자"
            elif q == "x":
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
            else:
                continue
        else:
            if id_number[7] not in ["1" , "2"]:
                print("잘못된 번호입니다.")
            else:
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
        year = id_number[:2]
        mon = id_number[2:4]
        try:
            print(f"{year}년{mon}월 {gender}")
        except:
            print("올바른 번호를 넣어주세요")
        break
