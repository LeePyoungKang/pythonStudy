#1. 반복문
#(1) for 변수 in 순환가능한 변수:
#range(시작값, 마지막값, 증감값)
for i in range(1, 10) : #증감값은 1이 디폴트
    print(i, end = ',')     
    #1,2,3,4,5,6,7,8,9,>>>

for i in range(1, 10, 2) : 
    print(i, end = ',')     
    #1,3,5,7,9,>>>

for i in range(10, 0, -1) :
    print(i, end = ',')     
    #10,9,8,7,6,5,4,3,2,1,>>>

for i in range(10) : #시작값 생략시 0 디폴트
    print(i, end = ',')     
    #0,1,2,3,4,5,6,7,8,9,>>>

print(list(range(10, 0, -1)))   
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

str1 = "Hello World~!"
for i in str1 : 
    print(i, end = ',') 
    #H,e,l,l,o, ,W,o,r,l,d,~,!,>>>

numList = [1, 2, 3, 4, 5]
total = 0
for i in numList :
    total += i 
    print(i, end = ',') 
print(total)
    #1,2,3,4,5,>>>
#15

#1~100사이의 숫자중 짝수만 출력
for i in range(1, 101) :
    if i % 2 == 0 :
        print(i, end = ',')
        
#조건문
#년도를 입력받아서 윤년 또는 평년 판단하여 출력
#윤년 조건 아래 두 조건을 모두 만족해야함
#(1) 년도가 4로 나누어 떨어져야 함
#(2) 년도가 100으로 나누어 떨어지지 않거나, 년도가 400으로 나우어 떨어져야함
#EX) 4(윤년), 100(평년), 400(윤년)
#and 연산자, or 연산자 활용
#if (조건1) and (조건2) :
#if (조건1) or (조건2) :

year = int(input("연도를 입력하시오: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) :
    print(f"{year}는 윤년입니다.")
else :
    print(f"{year}는 평년입니다.")

#and: 둘 다 참이여야 참이고, 하나라도 거짓이면 거짓
True and True
True and False
False and False

#or: 하나라도 참이면 참, 둘 다 거짓이여야 거짓

#높이가 10인 삼각형 만들기
#(1) 별이 먼저 채워지는 직각 삼각형
heigh = 10
for i in range(1, heigh + 1) :
    print('*' * i)

#(2) 공백이 먼저 채워지는 직각 삼각형
heigh = 10
for i in range(1, heigh + 1) :
    print(' ' * (heigh - i) + '*' * i)

#(3) 피라미드 삼각형
# %%
heigh = 10
for i in range(1, heigh + 1) :
    print(' ' * (heigh - i) + '*' * (2 * i - 1))

#(4) 다이아몬드
heigh = 10
for i in range(1, heigh + 1) :
    print(' ' * (heigh - i) + '*' * (2 * i - 1))
for i in range(heigh - 1, 0, -1) :
    print(' ' * (heigh - i) + '*' * (2 * i - 1))

#Better Comments 주석의 색상을 바꿔주는 확장 기능
#TODO
#!
#*
#?

#Jupyter 블럭 단위로 실행할 수 있는 확장 기능

# %%
