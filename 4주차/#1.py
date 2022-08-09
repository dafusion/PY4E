#Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.
#하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

def make_comma(number):
    number = str(number)
    length = len(number) 
    num_comma = length // 3 
    if length % 3 ==0: 
        num_comma = num_comma -1

    new_number = "" 
    n = -1
    while num_comma != 0:
        new_number = number[n] + new_number
        if  n % 3 == 0:
            new_number = "," + new_number
            num_comma = num_comma - 1
        n = n - 1
    print(number[:n+1]+new_number)
