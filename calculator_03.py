'''
날짜 : 20.12.27
직접만든 계산기

수정사항
    if, continue문을 사용하여 6이상을 입력할시 다시 질문하도록 설정했다.
    try-catch문을 사용하여 잘못된 입력시 "입력 오류가 발생하였습니다" 메시지를 출력하게 만들었다.

'''
def select(type):
    x,y = 0, 0
    try:
        x, y = map(int, input("계산하고 싶은 숫자를 차례대로 입력하세요(공백사용) ex) 1 5 , 2 6\n").split())
    except:
        print("입력 오류가 발생하였습니다")
    return x, y

while(1):
    choose = int(input("1.덧셈 / 2.뺄셈 / 3.곱셈 / 4.나눗셈 / 5.종료\n"))
    if choose >5:
        print("제대로 된 값을 입력해주세요!")
        continue
    if (choose==1):
        x, y = select("덧셈")
        print(f"덧셈: {x}+{y}는 {x+y}입니다")
    elif (choose==2):
        x, y = select("뺄셈")
        print(f"뺄셈: {x}-{y}는 {x+y}입니다")
    elif (choose==3):
        x, y = select("곱셈")
        print(f"곱셈: {x}*{y}는 {x+y}입니다")
    elif (choose==4):
        x, y = select("나눗셈")
        print(f"나눗셈: {x}/{y}는 {x+y}입니다")
    elif (choose==5):
        print("종료합니다")
        break

