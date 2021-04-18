# 20210413(화) - 2일차 수업

'''
< 숫자의 종류 (진법에 따른)>
1. 사람 - 10진수(0~9 한자리)
2. 컴퓨터 - 2진수(0~1 한자리), 8진수(0~7 한자리),
16진수(0~15 한자리) : 0~F 한자리
0~9, A:10, B:11, C:12, D:13, E:14, F:15

10진수 -> 2진수
2진수 -> 10진

'''
# 10진수(decimal)
a = 10
print(a)

# 2진수(binary) 0b: 2진수 취급, 0: 문자로 안보고 숫자로 본다
b = 0b1011
print(b)

# 8진수(octal)
c = 0o11
print(c)

# 16진수(hexadecimal)
d = 0x11
print(d)

print("--------")
print(187)
print(0b10111011)
print(0o273)
print(0xbb)

'''
-- escape code (이스케이프 코드)
\n : 줄바꿈 문자, 개행 문자
\t : 탭 간격
\\ : 문자로 \ 출력
\' : 문자로 ' 출력
\" : 문자로 " 출력
\a : 삑소리르 출력
\b : 백스페이스
'''
print("\\")
print("\'")
print("\"")

'''
< 데이터 타입의 종류 > : data type(자료형)
1. 숫자형 : 정수(int), 실수(float, 부동소숫점형)
2. 문자열형 : 쌍따옴표, 홀따옴표로 감싼 데이터, str
3. 논리형(bool, 불형, boolean형, 불린형)  : True(참), False(거짓) 의 값을 가지는 데이터
-----
4. 리스트(list)
5. 튜플(tuple)
6. 집합(set)
7. 딕셔너리(dictionary)

< 변수와 상수 >
1. 변수(Varoable) : 변하는 수, 메모리상에서 값을 저장하는 공간
a = 10
a = 20
2. 상수(Constant) : 변하지 않는 수
10
3.14

10 = 20 # 오류, 에러


'''
print("------------")
# 논리형
a = True
b = False
print(a)
print(b)
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>
print(30 > 10) # True
print(30 < 10) # False

'''
# 파이썬에서 모든 데이터는 참과 거짓으로 나누어짐.
1. 0이 아닌 모든 숫자(정수, 실수), 문자열 : True
2. 0, 빈 문자열(""), None : False

# bool() 함수: 데이터의 참과 거짓을 판별하는 함수
'''
a = 10
b = 3.14
c = 0
d = "python"
e = ""        # 빈 문자열
f = None      # 데이터가 없음
print(a)
print(type(a), ":", bool(a))
print(b)
print(type(b), ":", bool(b))
print(c)
print(type(c), ":", bool(c))
print(type(d), ":", bool(d))
print(e)
print(type(e), ":", bool(e))
print(f)
print(type(f), ":", bool(f))

'''
< 변수명을 만드는 규칙 (변수 명명법) >
-- 반드시 지켜야 하는 규칙.
1. 영어 대소문자, 숫자, 기호(_) 사용가능.
2. 공백 사용 불가.
3. 영어 대소문자는 구분해서 사용.
4. 숫자는 첫글자로는 사용하지 않음.
5. _(언더바) 이외의 기호는 사용불가

-- 권장하는 규칙
1. 유니코드(unicode)를 지원하므로 한글 사용이 가능하지만, 권장하지 않음.
2. 변수의 이름을 만들때는 의미있게 생성

< 변수 표기법 >
최고점수를 저장하는 변수 (97점이라고 가정)
s = 97
score = 97
maxscore = 97
max_score = 97 # 스네이크 표기법(snake notation) - 파이썬, 자바스크립트, html, css
maxScore = 97  # 카멜 표기법(camel notation) - 주로 자바 계열(JAVA, JSP, Spring, Andrid...)
'''
a = 10
A = 20
print(a, A)

age = 25
score = 90

'''
< 입출력 방법 >
1. 입력 : input() 함수
2. 출력 : print() 함수

print(출력내용 [,sep=구분자][.end=끝문자])
- ,(콤마) : 출력할 데이터를 연결함.
- sep 옵션 : 구분자, 출력할 때 변수들의 구분자(seperator)
- end 옵션 : 끝문자, 마지막 데이터 다음에 출력하는 문자 
'''
#age = input("당신의 나이를 입력하시오: ")
#print("나이:", age)
print("--------------")
a = 2021
b = 4
c = 13
print(a, b, c)
print(a, "-", b, "-", c,) # 2021 - 4 - 13
print(a, b, c, sep="-")  # 2021-4-13

d = "python"
e = "is"
f = "fun"
print(d, e, f)

s1 = "서울"
s2 = "대전"
s3 = "대구"
s4 = "부산"
print(s1, s2, s3, s4)
print(s1, s2, s3, s4, sep=" 찍고 ")

s5 = "바다구경"
print(s1, s2, s3, s4, s5, sep=" 찍고 ", end="@@@")
print()

print(s5)
#del(s5) # 변수 삭제
#del s5
print(s5)
print("------------")


'''
# input() 함수를 통해 입력받는 값은 문자열
# int() 함수 : 문자열을 정수로 변환하는 함수
# float() 함수 : 문자열을 실수로 변화하는 함수
kor = float(input("국어점수 입력: "))
mat = float(input("수학점수 입력: "))
tot = kor + mat
#tot = int(kor) + int(mat)
print("국어:", kor)
print("수학:", mat)
print("총점:", tot)
'''

# 문자열 연결
s1 = "one""two""three"
s2 = "python" + "is" + "good!" # 권장, 문자열 연결
s3 = ("one"
"two"
"three")
s4 = "사랑" * 3 # 3번 반복 
print(s1)
print(s2)
print(s3)
print(s4)

# 숙제 : 과일이름, 과일가격, 구매수량 입력받아서 출력하는 프로그램을 작성하시오.














