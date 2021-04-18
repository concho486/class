# 2021/04/16(금) - 5일차 수업

'''
데이터 타입(data type, 자료형)
- 숫자(정수, 실수), 문자열, 논리형,
- 컬렉션(리스트, 튜플, 셋, 딕셔너리)

컬렉션(Collextion)
- 여러 개의 값을 모아서 한꺼번에 처리할 수 있도록 하는 자료형

1. 리스트(List) - 여러 개의 값을 모아서 저장, 가변적인 배열

'''

'''
# 단일 리스트
a = [10, 20, 30, 40, 50]

# 리스트 순서는 0번부터 시작
# 리스트의 순서번호: 인덱스(index)
# 5개의 데이터 : 0번 ~ 4번
# n개의 데이터 : 0번 ~ n-1

print("--- 전체 리스트 ---")
print(a)
print(a[0:5])
print(a[0:])
print(a[:5])
print(a[:])

print("--- 인덱싱 ---")
# 인덱싱(indexing) : 특정값 1개를 추출하는 방법
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#print(a[5]) # IndexError: list index out of range
print(a[-1]) # 인덱스 번호의 -1은 마지막 요소

print("--- 슬라이싱 ---")
# 슬라이싱(slicing) : 범위의 값을 추출하는 방법
print(a[0:2]) # [10, 20], 0번에서 1번까지
print(a[2:4]) # [30, 40], 2번에서 3번까지
print(a[2:5]) # [30, 40, 50], 2번에서 4번까지
print(a[2:])  # [30, 40, 50], 2번에서 끝까지
print(a[1:])  # [20, 30, 40, 50], 1번에서 끝까지
print(a[0:4]) # [10, 20, 30, 40], 0번에서 3번까지
print(a[:4])  # [10, 20, 30, 40], 처음부터 3번까지
'''

'''
print("-------------")
# 이중 리스트 - 많이 사용
b = [10, 20, 30, ["A", "B", "C", "D"], 40, 50]

print(b)

# 인덱싱
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[3][0])
print(b[3][1])
print(b[3][2])
print(b[3][3])
print(b[-1]) # -1은 마지막 요소, 50
print(b[3][-1]) # D
print(b[-2]) # 40
print(b[-3]) # ['A', 'B', 'C', 'D']

print("-------------")
# 슬라이싱
print(b[1:4])
'''

'''
print("-------------")
# 삼중 리스트 - 많이 사용하지는 않음
c = [10, 20, 30, ["A", "B", "C", ["Pythone", "is", "fun"], "D"], 40]

print(c[3])
print(c[3][0])
print(c[3][2])
print(c[3][3])
print(c[3][3][2])
'''

# 리스트 연산 - 리스트끼리의 연산
a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9]
c = a + b # 리스트를 연결
print(a)
print(b)
print(c)

d = a * 3 # 리스트를 반복
print(d)

# e = a - b # error

print(type(a))
# c= a + 3 # error

print("--------------------")
a = [1, 2, 3, 4, 5, 6]

# 리스트 요소의 값을 수정
a[0] = 7
print(a) # [7, 2, 3]

# 인덱스 요소 1개 삭제
# del(a[1])
del a[1]    # [7, 3, 4, 5, 6]
print(a)

# 인덱스 요소 여러 개를 삭제
del a[1:4]  
print(a)    # [7, 6]

# 리스트에 값을 추가
# 1. append(값) 함수 - 리스트의 맨 뒤에 값을 추가하는 함수
# 2. insert(인덱스, 값) 함수 - 리스트의 해당 인덱스에 값을 추가하는 함수
a.append(8)
print(a) # [7, 6, 8]
a.append(9)
print(a) # [7, 6, 8, 9]

a.insert(1, 10)
print(a) # [7, 10, 6, 8, 9]
print("--------------------")

a = [1, 2, 3, 4, 5]
a.append(6) # 1개의 값 추가
print(a) # [1, 2, 3, 4, 5, 6]

# a.append(7, 8, 9) # error : 여러 개의 값을 추가하는 것은 불가
# 리스트에 하나의 요소를 추가 -> 이중 리스트
# a.append([7, 8, 9]) # [1, 2, 3, 4, 5, 6, [7, 8, 9]]
a += [7, 8, 9] # a = a + [7, 8, 9]
print(a)

# len() 함수 : 길이를 알려주는 함수
print(len(a))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 리스트에서 값을 삭제하는 방법
# 1. del() 함수 - 인덱스로 삭
# del(a[4])   # [1, 2, 3, 4, 6, 7, 8, 9], 4번 인덱스인 5를 삭제

# 2. remove() 함수 - 값을 삭제, 리스트의 멤버함수
# a.remove(4) # [1, 2, 3, 5, 6, 7, 8, 9], 4라는 값을 삭제
print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 3. pop() 함수 - 인덱스를 통해 값을 삭제, 리스트의 멤버함수
a.pop()  # 맨 뒤 요소의 값을 삭제
print(a) # [1, 2, 3, 4, 5, 6, 7, 8]

a.pop(4) # 4번 인덱스의 값을 삭제
print(a) # [1, 2, 3, 4, 6, 7, 8]
print("-------------------")

# 리스트의 정렬(sort)
a = [2, 4, 1, 5, 3]
print(a)

a.sort() # 오름차순 정렬
print(a)

a.sort(reverse=True) # 내림차순 정렬
print(a)

# 리스트의 거꾸로 뒤집기(reverse)
a = ["Life", "is", "too", "short"]
print(a)

a.reverse()
print(a)
a.reverse()
print(a) # ['Life', 'is', 'too', 'short']

# 리스트의 값에 대한 인덱스 확인
print(a.index("too"))

# 리스트의 문자열을 정렬
# 문자열은 알파벳순으로 정렬
a.sort() # 오름차순 정렬, 대문자가 소문자보다 앞에 온다.
print(a) # ['Life', 'is', 'short', 'too']

a.sort(key=str.lower)
print(a)
print("---------------------------")

'''
모든 데이터에 사용할 수 있는 함수 - print, len, int, input
print(10)
print("hello")

a = [1, 2, 3, 4, 5] # 리스트
리스트에만 사용할 수 있는 함수 - a.append(), a.remove()
'''

# 리스트에서 특정값이 포함된 갯수 구하기
a = [1, 2, 3, 4, 5, 1, 1, 2]
print("갯수:", len(a))
print("1의 갯수:", a.count(1))
print("2의 갯수:", a.count(2))

a = [1, 2, 3]

'''
# 복합대입 연산자, 결합 연산자, 할당 연산자
# +=, =+, *=, /=, %=, //=, &=, |=, ^= ...


'''
# 변수
a = 10
a += 5
# a = a + 5
print(a)

# 리스트
# 리스트를 연결하는 함수 - extend()
a = [1, 2, 3]
a.extend([4, 5])
# a += [4, 5]
# a = a + [4,5]
print(a)

# 빈 리스트를 만드는 방법
#a = [] # 빈 리스트
a = list()
print(a, type(a)) # [] <class 'list'>

# 문자열
a = "Good"
a += " Lcuk!"
# a = a + " Luck!"
print(a)

# 리스트의 활용
# A반 학생의 점수가 들어 있는 리스트
# A반 학생의 총점과 평균 점수를 확인하시오.
scores = [82, 77, 65, 98, 50, 70, 62, 87, 93, 55, 48, 85]

'''
# 1번 - for문, range() 함수
tot = 0
for i in range(len(scores)): # i: 0~9
    tot += scores[i]

print("총점: {}\n평균: {:0.2f}".format(tot, tot/len(scores)))
'''

'''
# 2번 - while문
tot = 0
i = 0
while i < len(scores):
    tot += scores[i]
    i += 1

print("총점: {}\n평균: {:0.2f}".format(tot, tot/len(scores)))
'''

# 3번 - for문(처음부터 끝까지라는 전제하에 사용)
# 리스트는 for문에서 range()함수 자리에 사용할 수 있음
tot = 0
for i in scores: # i: scores 리스트의 각각의 값
    tot += i

print("총점: {}\n평균: {:0.2f}".format(tot, tot/len(scores)))

'''
# < 리스트, 반복문, 조건문을 활용한 과제 >
# A반 학생의 점수가 들어 있는 리스트
scores = [82, 77, 65, 98, 50, 70, 62, 87, 93, 55, 48, 85]

# 문제1) A반 학생 중에서 최고점수와 최저점수를 구하시오.


# 문제2) A반 학생의 시험의 통과 여부를 출력하시오.
# 60점 이상이면 PASS, 60점 미만이면 FAIL
# -- 출력화면 설계
1번 학생은 82점으로 PASS입니다.
...
5번 학생은 50점으로 PAIL입니다.
...
12번 학생은 85점으로 PASS입니다.

# 문제3) A반에서 60점 미만인 학생을 제외하고 총점과, 평균을 구하시오.


# 문제4)  학생수를 입력받고, 학생수만큼의 점수를 입력받아서 총점, 평균,
# 최고점수, 최저점수를 구하는 프로그램을 작성하시오.
scorees = []


'''
























































































