# 주석(comment): 간단한 메모, 실행X
# 1. 출력 함수(print)
# - ()안의 값을 출력
# - 변수값 확인 용도로 많이 사용

printf("=" * 200)

# 문자열 타입(string Type)
# - Python: '' or "" -> string
# - c, java: ''(char), ""(String)/
printf("=" * 200)
#참고: Escape code
# - 문법: \(역 슬러쉬) + @
# 문자열(string) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기  ( 자주 사용 안 함)
# - 예) \n 한 wnf rogod, \t: 탭(8칸 공백)
print("Hello \nPython")
print("Hello \tPython")



# 2.자료형(Type)
# - python의 모든 자료형은 객체(Object)
# - Java 정수형: byte, short, int, long
# - python 정수형: int
#1) 문자형(String): "hHello", 'hi'
#2) 정수형(int): 3, -1, 0
#3)실수형(float): 3.14, 0.0, -2.2
#4) 논리형(boolean): True, False (앞글자 무조건 대문자.)

# 설명: 동일한 Type에서 다양한 종휴의 자료형을 사용하는 이유?
# - 매모리(저장공간)을 효율적으로 사용하기 위해서!
# - 대부분 만들어진지 오래 된 언어는 다양한 종류의 자료형 사용!
# - 자료형은 저장 할 수 있는 크기의 범위가 지정
# - 가정: (-10000 ~ 10000)
# - 가정: short(-100 ~ 100)
# - 특정 값: 0~9 -> 어떤 Type을 사용하면 효율적일까요? short

# 3. 동적 타이핑 언어(Dynamic Typing Language)
# - Java: int num + 4;
# - Python: num = 4(Type 지정X)
#- 코드가 실행될 때 자종으로 Type을 지정
#- type() 함수: ()안의 type을 확인할 때 사용
print("=" * 200)
print(type("abc"))



#4. 형 번환( type casting_
# - Type casting을 사용하면 값을 원하는 자료형으로 변환 가능
# - 1) int(): 정수형으로 변환
# - 2) float(): 실수형으로 변환
# - 3) str(): 문자열형으로 변환
print("=" *200)
# "Hi" -> float(), int() 불가!
# 문자열 실수형: "3.14"   가능!
# 문자열 정수형: "5"       가능
int_a = 2
float_b = 3.14
str_int_c = "9"
str_float_d = "9.2"
# 큰자료형 -> 작은 자료형으로 변환할 때 주의!
# 정수형(3) -> 실수형(3.0)
# 실수형(3.14) -> 정수형(3)  # 주의! (파일 손실 생김)
print(float(int_a))
# 문자열 정수형("3") -> 정수형(3)
# 문자열 정수형("3") -> 실수형(3.0)
# 문자열 실수형("3.14") -> 정수형(error)
# 문자열 실수형("3.14") -> 실수형(3.14)



#5. None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 하고 생성할 때 사용
print("="*200)
# C, Java: 변수생성 -> int num;
# Python: 변수생성 -> num(error)
# Python: 변수생성 -> num = None
student_name = none   # 절대 사용금지!
student_name = ""   # 적극 권장!



# 기본 자료형( primitive Type)
# - int num = 4;
#객체 자료형(Reference Type)  변수에 값이 위치한 "주소" 가 저장
# - String name = "10";

# - Java와 C: 기본, 객체 둘 다 사용
# - Python:  객체만 사용

#3 6.변수( variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간
print("="*200)
num = 4
num = 10
print (num) # 출력: 10
# - 변수 생성 및 초기화
# 문법: num = 5
#   * num: "num" 변수생성
#   * 대입연산자(=): 우측의 값을 좌측에 저장
#   * 동등연산자(==): Equal
#   * 초기화: 초기 변수를 생성하면 쓰레기 파일들이 존재
#            변수에 값을 대입하면 공간이 초기화 되고 값만 저장!