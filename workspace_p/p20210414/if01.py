# 2021/04/13(수) - 3일차 수업

'''
< 조건문과 반복문 >
1. 조건문
if문 : 조건의 내용이 참일 때, 거짓일 때에 대해서 선택해서 행동을 하도록 하는 명령문


파이썬에서는 블럭(단계)의 구분을 들여쓰기 구분 - 파이썬은 {} 기호가 너무 쓰이는게 싫어서
{} 대신 들여쓰기를 쓰는 것이다.
ex)                                            
if(n > 0):
    print()
    
java의 경우 {}를 쓴다.
ex)
if(n > 0) {
    print();
}
'''
# :(콜론), ;(세미콜론)
n = int(input("정수 입력:"))
'''
# 1번 - 1가지 조건, if문 하나만 활용
if n > 0
    print("양수입니다.")
    
# 2번 - 2가지 조건, if ~ else 활용
if n > 0:
    print("양수입니다.")
else:
    print("음수입니다.")

# 3-1번 - 3가지 조건, if ~ elif ~ else 활용
if n > 0:
    print("양수입니다.")
elif n < 0:
    print("음수입니다.")
else:
    print("0입니다.")
    
# 3-2번 - 3가지 조건
if n > 0:
    print("양수입니다.")
elif n < 0:
    print("음수입니다.")
elif n == 0:
    print("0입니다.")

# 4가지
if 조건식:
    실행문
elif 조건식:
    실행문
elif 조건식:
    실행문
else:
    실행문
'''

# < 조건문 확인 학습 >
# 문제1) 정수 한개를 입력받아서, 짝수인지, 홀수인지를 판별하는 프로그램을 작성하시오.
if n%2==1:
    print("홀수입니다.")
else:
    print("짝수입니다.")


# 문제2) 정수 한개를 입력받아서, 3의 배수이면서 4의 배수인지를 판별하는 프로그램을 작성하시오.
n = int(input("정수 입력:"))
if n*3==3**:
    print("3의 배수입니다.")
elif n*4==4**:
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



































