#8_자료구조 활용.py

#%%
#(1) 데이터의 중심 지표를 구하기
#데이터의 중심 지표 - 데이터를 대표하는 하나의 값
#ex) 평균, 최빈값, 중앙값

numList = [1, 2, 3, 1, 2, 1, 1, 3, 3, 3, 100]
#1) 평균
avg = sum(numList) / len(numList)
print(avg) #10.9

#2) 최빈값
num_set = set(numList)
num_dict = dict()
for n in num_set :   
    num_dict[n] = numList.count(n)
print(num_dict)

max_num = max(num_dict.values())
modes = []
for k, v in num_dict.items() :
    if v == max_num :
        print('최빈값', k,v)
        #mode = k
        modes.append(k)   #최빈값을 하나만 구하고 싶을때
        #break
print(modes)

#3) 중앙값
#리스트를 오름차순으로 정렬한 후,
#리스트의 크기를 N이라고 할때, 다음의 인덱스 값이 중앙값
#N이 홀수인 경우: N//2 인덱스 값
#N이 짝수인 경우: (N//2, N//2-1) 인덱스 값들의 평균
numList.sort() #기존 리스트를 변경해서 정렬
#sorted(numList) #정렬된 리스트를 반환, 기존 리스트 변경x

size = len(numList)
if size % 2 == 1 :       # 123  4  567 
    midVal = numList[size//2]
else :
    midVal = (numList[size//2] + numList[size//2-1])/2      #123  4사이의 평균5  678
print('중앙값:', midVal)


# %%
#2) set 예제
dateList = ['09/10', '09/11', '09/12', '10/01', '10/13', '11/20']

#위의 헬스장 이용 횟수 데이터에서 
#달별 이용 횟수를 출력하시오.

#2-1) 유니크한 달 값 구하기 (달만 있는 list 만들기, set 활용)
monList = []    #달을 담을 수 있는 리스트 선언
for d in dateList :
    monList.append(d[:2])   #앞에 두글자만 가져옴
monList = [d[:2] for d in dateList] #위랑 같은 표현
monList = [d.split('/')[0] for d in dateList]
#2-2) 달별 이용 횟수 구하기 (dict 및 count() 함수 활용)
monSet = set(monList)
monCount = list()   #dict() 이걸 집어넣어도 됨
for m in monSet :
    monCount.append((m, monList.count(m)))
print(monCount)
#-----------------------------------------
#빈도수 구하는 모듈
from collections import Counter
#collections 라이브러리에서 Counter 클래스 사용    
monCount = Counter(monList)
print(monCount)
print(monCount.most_common(1)) #가장 빈도수 높은 것 1개
print(monCount.most_common(3)) #가장 빈도수 높은 것 3개

counter1 = Counter(['사과', '사과', '딸기'])
counter2 = Counter(['포도', '포도', '딸기'])
print(counter1, counter2)
#집합 연산 가능
print(counter1 + counter2) #합집합
print(counter1 - counter2) #차집합
print(counter2 - counter1)
print(counter1 & counter2) #교집합
