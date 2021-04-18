# 2021/04/16(금) - 5일차 수업


# < while 문 연습 > : 초깃값, 조건식, 증감값
# 문제1) 정수를 1개 입력받아서, 1부터 입력받은 수까지 중에서 짝수를 출력하고,
# 짝수의 합을 출력하시오.
'''
n = int(input("정수 입력 :"))

i = 1 # 초깃값
tot = 0

while i <= n: # 조건식
    if i%2 == 0:
        print(i)
        tot += i # tot = tot + i
    i += 1 # i = i + 1, 증감값

print("1부터 {}까지의 짝수의 합 : {}".format(n, tot))
'''


# 문제2) 정수를 1개 입력받아서, 1부터 입력받은 수까지 중에서
# 3의 배수이면서 4의 배수를 출력하고, 그 갯수와 합을 출력하시오.
'''
n = int(input("정수 입력 :"))

i = 1 # 초깃값
tot = 0
cnt = 0

while i <= n:
    if i%3==0 and i%4==0:
        print(i)
        tot += i
        cnt += 1
    i += 1

print("1부터 {}까지의 3의 배수이면서 4의 배수의 합 : {}".format(n, tot))
print("1부터 {}까지의 3의 배수이면서 4의 배수의 갯수 : {}".format(n, cnt))
'''

# 문제3) 구구단의 단을 입력받고, 입력한 단의 구구단을 출력하시오.
'''
n = int(input("구구단의 단 입력 : "))

i = 1 # 초깃값
while i <= 9: # 조건식
    print("{} * {} = {}".format(n, i, n*i))
    i += 1 # 증감값
'''
# 중첩 반복문
# 문제4) 2단부터 9단까지를 모두 출력하시오.

i = 2 # 단, 2~9
j = 1 # 곱하는 수, 1~9

while i <= 9:
    print("=== {}단 ===".format(i))
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1


'''
< 과제 >
# if문 활용
문제1) 정수 2개와 산술연사자를 입력받아서 계산하는 계산기 프로그램을 작성하시오.
--입력화면
정수1 입력: 10
정수2 입력: 5
연산자 입력: *

--출력화면
10 * 5 = 50
'''
'''
n1 = int(input("정수1 입력: "))
n2 = int(input("정수2 입력: "))
op = input("연산자 입력: ")

result = 0

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    result = n1 / n2
else:
    print("연사자를 잘못 입력하였습니다.")

print("{} {} {} = {}".format(n1, op, n2, result))
'''

'''
# if문 활용
문제2) 정수 1개를 입력받아서 1자릿수, 2자릿수, 3자릿수 이상인지를 판별하는
프로그램을 작성하시오.

-- 입력화면
정수 입력 : 15

-- 출력화면
15는 2자릿수입니다.
'''
'''
n = int(input("정수 입력: "))

# 1번
if n < 10 and n > -10:
    print("{}은(는) 1자리수입니다.".format(n))
elif n < 100 and n > -100:
    print("{}은(는) 2자리수입니다.".format(n))
elif n < 1000 and n > -1000:
    print("{}은(는) 3자리수입니다.".format(n))


# 2번 - 파이썬에서는 수학식처럼 사용하는 것을 허용
if -10 < n < 10:
    print("{}은(는) 1자리수입니다.".format(n))
elif -100 < n < 100:
    print("{}은(는) 2자리수입니다.".format(n))
elif -1000 < n < 1000:
    print("{}은(는) 3자리수입니다.".format(n))
'''

'''
# 반복문 활용
문제3) 팩토리얼(factorial)을 구하는 프로그램을 작성하시오.
ex) 5! = 1 * 2 * 3 * 4 * 5 = 120

-- 입력화면
정수 입력 : 5

-- 출력화면
5! = 1*2*3*4*5 = 120
'''

'''
n = int(input("정수 입력: "))


# 1번 - for문 활용
fat = 1

for i in range(1, n+1):
    fat = fat * i

# 2번 - while문 활용 : 초깃값, 조건식, 증감값
fat = 1
i = 1 # 초깃값

while i <= n: # 조건식
    fat *= i # fat = fat * i
    i += 1 # i = i + 1

print("{}! = {}".format(n, fat))
'''
'''
# 출력 화면 : 5! = 1 * 2 * 3 * 4 * 5 = 120
# 3번

n = int(input("정수 입력: "))
fat = 1
s = ""

for i in range(1, n+1):
    fat *= i
    s = s + str(i)
    if i < n:
        s = s + " * "

print("{}! = {} = {}".format(n, s, fat))
'''

'''
# 반복문 활용
문제4) 피보나치(fibonacci) 수열을 구하는 프로그램을 작성하시오.
피보나치 수열 : 앞의 두 정수를 더하여 다음 수를 만드는 

-- 입력화면
피보나치 수열 갯수 입력 : 10

-- 출력화면
1 1 2 3 5 8 13 21 34 55

'''
'''
n = int(input("피보나치 수열 갯수 입력 : "))

n1 = 1
n2 = 1
n3 = 0
s = ""

#print(n1, n2)
s= s + str(n1) + "" + str(n2) + " "
for i in range(n-2): # 10이라면 8, 8번 회전
    n3 = n1 + n2
    #print(n3)
    s = s + str(n3) + " "
    n1 = n2
    n2 = n3

print("피보나치 수열 {}개 : {} ".format(n, s))

'''




























