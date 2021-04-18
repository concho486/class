'''
< 아스키 코드와 유니코드 >
아스키 코드(ASCII code) American Standard Code for Infomation Interchange
- 컴퓨터에서 데이터의 전달을 위해 문자를 숫자로 표현할 수 있도록 약속해 놓은 코드
- 7비트로 표현 (0~127)
- C언어 - 아스키 코드 지원, 영어는 사용가능하지만, 한글 지원은 하지 않음
ex) A: 65 B: 66, a: 97, b:98

유니코드(unicode) - 아스키 코드를 포함해서 16비트 코드 체계로 확장.
- 2의 16승까지 지원, 65536문까지 지원
- 전세계 모든 문자를 지원

'''

# 아스키코드 확인
# ord() 함수 : 문자에 대한 아스키코드 값을 출력
# chr() 함수 : 아스키코드값에 대한 문자를 출력
print("a", ":", ord("a"))
print(65, ":", chr(65))

'''
Python : and, or, not
Java   : &&, ||, !
R      : &, |, !
oracle : and, or, not

* : 아스테리스크(asterisk)
& : 앰퍼샌드(ampersand)
| : 파이프(pipe)
~ : 틸드(tilde)
^ : 캐럿(carat)

< 연산자의 종류 >
1. 대입 연산자 : =
2. 산술 연산자 : +, -, *, /(소숫점을 포함한 나눈 결과)
//(나누어서 몫), %(나누어서 나머지), **(승수)
3. 비교 연산자 : >, >=, <=, ==(equal, 같다), !=(not equal, 다르다)
- 비교 연산의 결과는 True(참) 또는 False(거짓)
4. 논리 연산자 : AND(이고, 면서), OR(이거나, 또는), NOT(논리 NOT, 논리 부정)
AND(논리 And) : 모든 항이 참일 때 전체 결과가 참, 하나라도 거짓이 있으면 전체 결과도 거짓
OR(논리 or) : 둘 중에 하나라도 참이 있으면 전체 결과도 참, 모두가 거짓이면 전체 결과도 거짓
NOT(논리 Not) : 참을 거짓으로, 거짓을 참으로 바꾸어 줌.
- 논리, 비교 연산자 자주 함께 사용되며, 우선순위는 비교 연산자 먼저 계산하고, 연산자를 계산
- 비교가 논리보다 우선순위가 높음
5. 부호 연산자: +(양수), -(음수)
6. 비트 연산자: &(비트 AND), |(비트 OR), ~(비트 NOT), ^(Exclusive OR, XOR, 배타적 OR)
- 비트 연산자는 2진수로 계산
& : 둘 다 1일 때 결과 1일 되는 연산자
| : 둘 중에 하나라도 1이 있을 때 1이 되는 연산자
^ : 둘 중 하나만 1일 때 견과가 1이 되는 연산자
~ : 0을 1로, 1을 0으로 반전시키는 연산자
7. 쉬프트 연산자 : <<, >>
<< : left shift 연산자, 2진수의 곱셋
>> : right shift 연산자, 2진수의 나눗셈

'''
print("--- 산술 연산자 ---")
a = 10; b = 3
print("a = ", a)
print("b = ", b)
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("a // b = ", a//b)
print("a % b = ", a%b)
print("2 ** 5 = ", 2**5)

print("--- 비교 연산자 ---")
print("a > b = ", a>b) # True
print("a < b = ", a<b) # False
print("a == b = ", a==b) # False
print("a != b = ", a!=b) # True

print("--- 논리 연산자 ---")
print(a>5 and b<5) # True
print(a>5 and b>5) # False
print(a<5 and b<5) # False
print(a>5 or b<5)  # True
print(a>5 or b>5)  # True
print(a<5 or b>5)  # False
print(not(a<5 or b>5)) # True

print("--- 비트 연산자 ---")
print("13 & 11 = ", 13 & 11) # 9
print("13 | 11 = ", 13 | 11) # 15
print("13 ^ 11 = ", 13 ^ 11) # 6

print("--- 쉬프트 연산자 ---")
print("2 << 3 =", 2 << 3)    # 16
print("32 >> 3 =", 32 >> 3)  # 4

