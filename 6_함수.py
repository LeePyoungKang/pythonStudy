# 6_함수

#%%
#(1) 원의 넓이를 구하는 함수
def getCircleArea(r) : #매개변수 r은 반지름 값
    return r * r * 3.14159

area1 = getCircleArea(10)
area2 = getCircleArea(4.2)
print(area1, area2)

#(2) 삼각형의 넓이를 구하는 함수
def getTriangleArea(base, height) :
    return base * height / 2

area1 = getTriangleArea(3, 4)
area2 = getTriangleArea(5.1, 6.3)
#area3 = getTriangleArea("3", "5") 들어간 매개변수가 문자형이라 안됨
print(area1, area2)

#(3) 출력이 없는 함수
def say_myself(name, age, man) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는{age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
    
say_myself('홍길동', 30, True)
say_myself('김하나', 24, False)

# %%
#함수의 매개변수 디폴트 값 설정
#디폴트 값을 설정한 매개변수는 함수의 입력 매개변수들 중 끝에 배치
def say_myself(name, age=-1, man=True) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는{age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("홍길동", 30) #man 매개변수 생략 가능
say_myself("김하나", man=False, age=27) #man 매개변수 이름으로 값 지정
say_myself("김현수")


# %%
#함수의 호출 방식
#(1) 매개변수에 값이 복사되어 호출 (Call by Value)
#(2) 매개변수에 주소값이 복사되어 호출 (Call by Reference0
# 
#(1)예제
def testFunc(num) :     #윗쪽의 num이랑 아랫쪽의 num은 다른 변수다
    num = 5

num = 10
testFunc(num)
print(num)      #10

#(2) 예제
def testFunc(numList) :
    numList.append(10)
    print(id(numList))     #위에 리스트랑 아래의 리스트의 주소값이 같음
    numList[0] = -100
    
aList = [1, 2, 3]
testFunc(aList)
print(id(aList))    #aList의 주소값 2893061594688
print(aList)

#(3)함수 내에서 함수 밖의 변수(기본타입 변수)를 사용하고 싶은 경우
def testFunc(num2) :    
    global num      #global => 전역변수
    num = 100

num = 10
testFunc(num)
print(num)      #100

# %%
#함수의 가변 인수
#가변인수: 매개변수의 개수가 정해져 있지 않고 사용하는 인수
#Ex) print(1, 2, 3, 4, 5)
def testFunc(*arg) :    # *은 가변인수
    print(arg)
    return sum(arg)

print(testFunc(10, 20, 30, 40))

#일반 매개변수와 가변인수가 같이 사용될 경우
#가변인수를 마지막 인수로 넣어줘야 한다.abs
def testFunc(str1, str2, *nums) :    
    print(str1, str2, nums)
    return sum(nums)

print(testFunc("Hi", "Bye", 10, 20, 30))

# %%
#재귀 함수: 자기 함수를 다시 호출하는 함수

def recursive(num=0) :
    print(f"{num}재귀 함수를 호출합니다.")
    recursive(num+1)

recursive(0)    #계속 호출하다가 오류가 남
#재귀함수는 반드시 종료조건을 명시해야한다.

# %%
def recursive(num=0) :
    print(f"{num}재귀 함수를 호출합니다.")
    if num == 100 :
        return -1   #함수는 return 문을 실행하면 종료 (-1자리에 아무거나 넣거나 안넣어도 자동으로 종료됨)
    recursive(num+1)
    

recursive(0)  

# %%
#재귀함수 활용
#(1) 팩토리얼
#ex) 5! = 5*4*3*2*1

#반복문 예시
def factorial(n) :
    result = 1
    for i in range(1, n + 1) :
        result *= i
    return result
print(factorial(5))

#재귀함수 예시
def factorial2(n) :
    if n <= 1 :
        return 1
    return n * factorial(n-1)
print(factorial2(5))
#5*factorial2(4)
#5*4*factorial(3)
#5*4*3*factorial(2)
#5*4*3*2*factorial(1)
#5*4*3*2*1 종료    
    
# %%
#(2) 피보나치 수열
# 1 1 2 3 5 8 13 ...
fibo = [0, 1]
n = 5
for i in range(2, n+1) :
    fibo.append(fibo[i-1] + fibo[i-2])      #전 두항을 더해서 새로운 항을 추가함
print(fibo)
print(fibo[-1])     #마지막 값을 알고싶을때 [-1]

#재귀함수 예시
def fiboFunc(n) :
    if n == 1 or n ==2 :
        return 1
    else :
        return fiboFunc(n - 1) + fiboFunc(n - 2)
print(fiboFunc(5))


#%%
#퀴즈) 숫자인 리스트를 받아, 평균값을 구하는 함수를 만드시오.
#Ex) input:[1, 2, 4] => result: 2.3333...
#numList = [1, 2, 3, 4]
#avg = sum(numList) / len(numList)



def getListAverage(numList) :
    return sum(numList) / len(numList)

print(getListAverage([1, 2, 3, 4, 5]))      #3.0

numList = [2, 4, 5]
print(getListAverage(numList))      #3.6666666666666665 


# %%
#합성 저항 구하는 함수.
def getTotalResis(rList, serial = True) :
    if serial :
        return sum(rList)
    else :
        result = 0
        for r in rList :
            result += 1 / r
        return 1 / result

#serial = True 직렬저항 값 리턴
#serial = False 병렬저항 값 리턴
#직렬저항 = 저항1 + 저항2 + 저항3...
#병렬저항 = 1/(1/저항1 + 1/저항2 + 1/저항3...)

print(getTotalResis([1, 2, 3 ,4])) #직렬저항
print(getTotalResis([1, 2, 3, 4], False)) #병렬저항


# %%
#요일을 구하는 함수
#입력: 년, 월, 일 (정수형)
#출력: 0~6 (0: 일요일, 1: 월요일, ... 6: 토요일)
#제라의 공식 이용: ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
#a=연도의 앞 2자리, b=연도의 뒤 2자리, c=월, d=일
#단, c의 값이 1,2일 경우 13, 14로 바꿔서 계산하고 년도를 1빼준다.

year, mon, day = 2023, 11, 2
a, b = divmod(2023, 100)    #나머지 연산자로 숫자 분리를 한다.
print(a, b)
if mon <= 2:
    mon += 12
    year -= 1
a, b = divmod(year, 100)
c, d = mon, day
print(a, b)
week = ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
print(week)

# %%
def YearMonDay(year, mon, day, kor_mode=False) :   #False가 기본값 안써도 상관 없음
    if mon <= 2 :
        mon += 12
        year -= 1
    a, b = divmod(year, 100)
    c, d = mon, day
    w = ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
    if kor_mode :
        #한글로 요일 표시
        week_kr = ["일", "월", "화", "수", "목", "금", "토"]
        return week_kr[w]
    else :
        return w
    
print(YearMonDay(2023, 11, 3))
print(YearMonDay(2023, 11, 3, True))


#%%
#(1) 달력 출력
#년도와, 달을 입력받아서 아래와 같이 출력
#     2023년도 11월     
# 일 월  화 수 목 금 토 
#          01 02 03 04 
# 05 06 07 08 09 10 11 
# 12 13 14 15 16 17 18 
# 19 20 21 22 23 24 25 
# 26 27 28 29 30 

def getWeek(year, mon, day, kor_mode=False) :   #False가 기본값 안써도 상관 없음
    if mon <= 2 :
        mon += 12
        year -= 1
    a, b = divmod(year, 100)
    c, d = mon, day
    w = ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
    if kor_mode :
        #한글로 요일 표시
        week_kr = ["일", "월", "화", "수", "목", "금", "토"]
        return week_kr[w]
    else :
        return w
    
def printCalendar(year, mon) :
    calendar = [[0]*7 for i in range(6)]
    # print(calendar) #6행, 7열

    # year, mon = 2023, 11
    lastDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mon == 2 :
        if (year%4==0) and (year%100!=0 or year%400==0) :
            lastDays[1] = 29

    start_idx = getWeek(year, mon, 1)
    # print(start_idx) #요일, 캘린더의 날짜 시작 위치

    #1~lastday까지 범위
    for i in range(1, lastDays[mon-1]+1) : #1~lastdat까지 범위
        #print(i, end=',')
        calendar[start_idx//7][start_idx%7] = i
                #행          #열
        # start_idx 0~6: r:0, 0~6
        # start_idx 7~13: r:1, 0~6
        # start_idx 14~20: r:2, 0~6
        start_idx += 1
    # print(calendar)

    #달력 출력: 리스트의 모든 요소를 출력
    title = f'{year}년도 {mon}월'
    print(f'{title:^20}') # ^: 가운데 정렬
    weeks = ['일', '월', '화', '수', '목', '금', '토']
    for w in weeks :
        if w == '일' :
            #빨간색
            print(f'\033[31m{w}\033[0m', end=' ')
        elif w == '토' :
            #파란색
            print(f'\033[34m{w}\033[0m', end=' ')
        else :
            print(f'{w}', end=' ')
    print()

    for r in range(len(calendar)) :    
        
        #한주 출력
        if sum(calendar[r]) == 0 :
            continue
        for c in range(len(calendar[0])) :
            
            #색깔 지정
            if c == 0 :
                print(f'\033[31m', end='')
            elif c == 6 :
                print(f'\033[34m', end='')
            
            #날짜 출력
            if calendar[r][c] == 0 :
                print(' '*2, end=' ')
            else:
                print(f'{calendar[r][c]:0>2}', end =' ')
            
            #색깔 초기화
            print(f'\033[0m', end='')
        print()
    
printCalendar(2022, 7)
printCalendar(2023, 2)

    

# 아래(3줄) 방식을 다르게 풀어서 쓴 코드 (더 복잡함)
#---------------------------------------------
#1 for i in range(1, lastDays[mon-1]+1) : 
#2     print(i, end=',')
#3     calendar[start_idx//7][start_idx%7] = i
#---------------------------------------------    
# start_idx = getWeek(year, mon, 1)
# write = False
# d = 1
# for r in range(len(calendar)) :
#     for c in range(len(calendar[0])) :
#         if r==0 and c==start_idx :
#             write = True
#         if write :
#             calendar[r][c] = d    
#             d += 1
#         if d+1 == lastDays[mon-1] :
#             write = False
#             break
# print(calendar)
            
            
#%%
#(2) 리스트컴프리헨션을 이용해서 병렬저항의 합성저항값을 출력
#입력 저항값 리스트 ex) [1, 2, 3, 4, ]
#출력 1.23
#리스트컴프리헨션을 이용해서 간결하게 함수를 만드시오

#for문을 쓴 방법
def getTotalResis(rList) :
    total = 0
    for r in rList :
        total += 1/r
    return 1/total
print(getTotalResis([1, 2, 3]))

#리스트컴프리헨션을 쓴 방법
def getTotalResis(rList) :
    total = sum([1/r for r in rList])
    return 1/total

#리스트컴프리헨션을 쓴 방법2 (더 간결하게)
def getTotalResis(rList) :
    total = 1/sum([1/r for r in rList])
print(getTotalResis([1, 2, 3]))
