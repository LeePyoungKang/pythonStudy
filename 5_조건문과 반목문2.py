# 5_조건문과 반목문2
#%%
#! 조건문: 삼항연산자
#*조건문의 축약 버전
#변수 = 참값 if 조건식 else 거짓값
num = 15
oddNum = "홀수" if num % 2 == 1 else "짝수"
print(oddNum)

#윗 버전의 일반 버전
if num % 2 == 1 :
    oddNum = "홀수"
else :
    oddNum = "짝수"
print(oddNum)

#지저분 하지만 이렇게 쓸 수도 있다라는 예시
score = 90
#scoreStr = "F" if score < 50 else ("E" if score < 60 else "D")
#print(scoreStr)
scoreStr = "F" if score < 50 else \
                "E" if score < 60 else \
                    "D" if score < 70 else \
                        "C" if score < 80 else \
                            "B" if score < 90 else \
                                "A" if score <= 100 else "F"        
print(scoreStr)     #A

# %%
#? break문과 continue문
#1) break: 특정 조건하에 반복문을 빠져나올때 사용
#2) coutinue: 특정 조건하에 반복문의 조건식으로 돌아갈때 사용

for i in range(1, 10) :
    if i == 5 :
        break
    print(i, end = ',')

#Ctrl + Enter 현재 셀 실행
#Alt + Enter 다음 셀 만들기

for i in range(1, 10) :
    if i % 2 == 0 :
        continue
    print(i, end = ',')

# %%   
#3) 반복문~else 문
#else: 반목문이 완전히 끝났을 때 마지막에 실행됨
for i in range(1, 10) :
    print(i, end = ',')
else :
    print("\n프로그램 종료")

for i in range(1, 10) : 
    if i == 3 :
        break   #중간에 빠져나오면 else가 실행이 안됨
    print(i, end = ',')
else :
    print("\n프로그램 종료")

# %%
#반복문 zip(), enumerate()
#zip(): 여러 리스트의 같은 인덱스끼리 묶어 리스트로 반환
#enumerate(): for문에서 인덱스와 같이 출력하고 싶을 때 사용

#    수학 영어 국어
s1 = [30, 20, 50] #첫번째 학생
s2 = [50, 60, 90] #두번째 학생
s3 = [10, 20, 40] #세번째 학생

#우리반 학생의 수학점수 총합과 평균
total_math = s1[0] + s2[0] + s3[0]
print(total_math)
total_math = sum(list(zip(s1, s2, s3))[0])
print(total_math)

#과목별 평균값
subject_avg = []
for scores in zip(s1, s2, s3) :
    print(scores)
    subject_avg.append(sum(scores) / len(scores))
print(subject_avg)

student_scores = [s1, s2, s3]
subject_avg = []
for scores in zip(*student_scores) :
    print(scores)
    subject_avg.append(sum(scores) / len(scores))
print(subject_avg)

# %%
colors = ['white', 'black', 'red', 'green']
for i, color in enumerate(colors) :
    print(i, color)
    
colors = ['white', 'black', 'red', 'green']
for i, color in enumerate(colors, start = 1) :  #인덱스 값을 1부터 시작하고 싶을때
    print(i, color)

# %%
#while 조건식
#반복 조건을 알때 사용
i = 0
while i < 10 :
    print(i)
    i += 1

#반복 횟수를 알거나 반복할 리스트가 있을 때 활용
for i in range(0, 10) : #위 아래 결과값 똑같음
    print(i)

# %%
#반복문 활용
#(1) 구구단 출력
for i in range(2, 10) :
    for j in range(1, 10) :
        print(f'{i} X {j} = {i * j}')
    print('-' * 10)

#(2) 숫자 사각형 출력
#4행, 5열
#row, col = 4, 5
#01 02 03 04 05
#06 07 08 09 10
#11 12 13 14 15
#16 17 18 19 20
num = 3
#print(f'{num : 02}') #'03' 출력됨, 02의미 : 자리수 2개 0으로 채움
row, col = 4, 5
for r in range(1, row + 1) :
    for c in range(1, col + 1) :
        print(f'{(r - 1) * col + c:02}', end = ' ')
    print()
    
#(3) 00:00:00 ~ 23:59:59초 출력
cnt = 0
for hour in range(24) :
    for min in range(60) :
        for sec in range(60) :
            cur_time = f'{hour}:{min}:{sec}'
            cnt += cur_time.count('50')     #50초가 총 몇번 나오는지 카운트
            print(cnt)
            print(f' {hour}:{min}:{sec}')

#(4) 입력된 숫자의 각 자리수의 합을 구하기
#12345 => 1+2+3+4+5
#문자열 활용한 방법
num = 12345
num_str = str(num)
print(list(num_str))
total = 0
for i in num_str :  #문자열의 특성상 num_str앞에 list를 안써도 됨
    total += int(i)
print(total)

#연산자를 이용해 해결한 방법
total = 0
num = 12345
while num != 0 :
    total += num % 10
    num = num // 10
print(total)

#%%
#(5) 돈을 입력받아서 잔돈을 출력
#500 > 3
#100 > 0
#50 >1
#10 >2
money = 1570
coins = [500, 100, 50, 10]

while money != 0 :
    if money % 500 : 
        coins[0] = money // 500 
    elif money % 100 : 
        coins[1] = money // 100 
    elif money % 100 : 
        coins[2] = money // 100 
    elif money % 100 : 
        coins[3] = money // 100 
    else :
        print("잔돈이 모두 나왔습니다.")
    
# %%

for z in range(1, 13) :
    for x in range(1, 32) :
        print(z,"월-", x,"일-")