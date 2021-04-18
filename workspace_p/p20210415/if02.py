# 2021/04/15(목) - 4일차 수업

'''

내가 푼 것

# < 조건문 확인 학습 >
# 문제1) 정수 한개를 입력받아서, 짝수인지, 홀수인지를 판별하는 프로그램을 작성하시오.
if n%2==1:
    print("홀수입니다.")
else:
    print("짝수입니다.")


# 문제2) 정수 한개를 입력받아서, 3의 배수이면서 4의 배수인지를 판별하는 프로그램을 작성하시오.
n = int(input("정수 입력:"))
if n%3==0:
    print("3의 배수입니다.")
elif n%4==0:
    print("4의 배수입니다.")
else:
    print("3과 4의 배수가 아닙니다.")



# 문제3) 국어, 영어, 수학 점수를 입력받아서, 총점, 평균, 학점을 구하는 프로그램을 작성하시오.
# 학점은 평균이 90점이상이면 A, 80점이상이면 B, 70점이상이면 C, 60점이상이면 D, 60점 미만이면 F

a = int(input("국어 점수:"))
b = int(input("영어 점수:"))
c = int(input("수학 점수:"))
sum = a + b + c
average = (a + b + c) / 3
print("총점: ", sum); print("평균: ", average)

if average > 90:
    print("A")
elif average > 80:
    print("B")
elif average > 70:
    print("C")
elif average > 60:
    print("D")
else:
    print("F")

# < 확인학습 >
# 문제1) 10진수 27을 2진수로 확인하고, 왼쪽으로 3비트 이동했을 때의 값과,
# 오른쪽으로 4비트 이동했을 때의 값을 계산하고, 파이썬 프로그램으로 확인하시오.

print(27)
print("2진수:", 11011)
print("27:", 0b11011)

print(0b11011 << 3)
print(27 << 3)

print(0b11011 >> 4)

# 문제2) 월을 입력받아서 계절을 판별하는 프로그램을 작성하시오.
# 3,4,5,월: 봄, 6,7,8월: 여름, 9,10,11: 가을, 12,1,2: 겨울

-- 입력화면 설계
월을 입력하세요. 6

-- 출력하면 설계
6월은 여름입니다.


n = int(input("월을 입력하세요.: "))

if n==3:
    print("봄")
elif n==4:
    print("봄")
elif n==5:
    print("봄")
elif n==6:
    print("여름")
elif n==7:
    print("여름")
elif n==8:
    print("여름")
elif n==9:
    print("가을")
elif n==10:
    print("가을")
elif n==11:
    print("가을")
elif n==12:
    print("겨울")
elif n==1:
    print("겨울")
elif n==2:
    print("겨울")
else:
    print("계절 월수가 아닙니다.")
'''


# 강사님이 풀어준 것
   
# < 조건문 확인 학습 >
# 변수, 함수, 연산자, if
# 문제1) 정수 한개를 입력받아서, 짝수인지, 홀수인지를 판별하는 프로그램을 작성하시오.
'''
n = int(input("정수를 입력하시오."))

-- 1번
if n%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

-- 2번
if n%2 == 0:
    print("짝수입니다.")
elif m%2 == 1:
    print("홀수입니다.")

-- 3번
if n%2 == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")
'''

# 문제2) 정수 한개를 입력받아서, 3의 배수이면서 4의 배수인지를 판별하는 프로그램을 작성하시오.
'''
n = int(input("정수를 입력하시오."))

if n%3==0 and n%4==0:
    print("3의 배수이면서 4의 배수입니다.")
else:
    print("3의 배수이면서 4의 배수가 아닙니다.")
'''

# 문제3) 국어, 영어, 수학 점수를 입력받아서, 총점, 평균, 학점을 구하는 프로그램을 작성하시오.
# 학점은 평균이 90점이상이면 A, 80점이상이면 B, 70점이상이면 C, 60점이상이면 D, 60점 미만이면 F
'''
kor = int(input("국어 점수 입력: "))
eng = int(input("영어 점수 입력: "))
mat = int(input("수학 점수 입력: "))

tot = kor + eng + mat
ave = tot / 3

if ave >= 90:
    grade = "A"
elif ave >= 80:
    grade = "B"
elif ave >= 70:
    grade = "c"
elif ave >= 60:
    grade = "D"
else:
    grade = "F"


#print("총점:", tot)
#print("평균:", ave)
#print("학점:", grade)
#print("총점:", tot, "\n", "평균:", ave, "\n", "학점:", grade)
#print("총점: {0:5d}\n평균: {1:8.2f}\n학점: {2}".format(tot, ave, grade))
print("총점: {}\n평균: {:0.2f}\n학점: {}".format(tot, ave, grade))
'''
# < 확인학습 >
# 문제1) 10진수 27을 2진수로 확인하고, 왼쪽으로 3비트 이동했을 때의 값과,
# 오른쪽으로 4비트 이동했을 때의 값을 계산하고, 파이썬 프로그램으로 확인하시오.
'''
print(27)
print(0b11011)
print(27 << 3) # 216
print(27 >> 4) # 1
'''

# 문제2) 월을 입력받아서 계절을 판별하는 프로그램을 작성하시오.
# 3,4,5,월: 봄, 6,7,8월: 여름, 9,10,11: 가을, 12,1,2: 겨울
month = int(input("월 입력: "))

'''
-- 1번
if month==3 or month==4 or month==5:
    print("봄")
elif month==6 or month==7 or month==8:
    print("여름")
elif month==9 or month==10 or month==11:
    print("가을")
elif month==12 or month==1 or month==2:
    print("겨울")
else:
    print("잘못 입력하였습니다.\n다시 시작해 주세요.")
'''
    
# 2번
if month>=3 and month<=5:
    print("{}월은 봄입니다.".format(month))
elif month>=6 and month<=8:
    print("{}월은 여름입니다.".format(month))
elif month>=9 and month<=11:
    print("{}월은 가을입니다.".format(month))
elif month==12 or month==1 or month==2:
    print("{}월은 겨울입니다.".format(month))
else:
    print("잘못 입력하였습니다.\n다시 시작해 주세요.")

'''
-- 3번 : 수학식 - 파이썬에서만 허용, 다른 거의 모든 프로그램밍 언어에서는 사용할 수 없음.
-- 권장하지 않음
if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
elif month==12 or month==1 or month==2:
    print("겨울")
else:
    print("잘못 입력하였습니다.\n다시 시작해 주세요.")
'''



'''
-- 입력화면 설계
월을 입력하세요. 6

-- 출력하면 설계
6월은 여름입니다.
'''













