#입력받기
calc = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계>" ))

#1번
if calc == 1:
    s = input("***수식을 입력하세요 :> ")
    answer = eval(s)
    print(s,"결과는 ",answer,"입니다.")

#2번 
if calc == 2:
    num1 = int(input("***첫 번째 숫자를 입력하세요 :> "))
    num2 = int(input("***두 번째 숫자를 입력하세요 :> "))
    sum = 0
    for i in range (num1, num2 + 1):
        sum = sum + i
    print(num1,"+...+",num2,"는 ",sum,"입니다.")