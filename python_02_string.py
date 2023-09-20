# 문자열의 이해(String)

# 1. 문자열 인덱스
#   - 문자열은 각 문자마다 순서(인덱스)가 있음
#   - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#   - 인덱스 시작은 0
#   - 인덱스는 공뱍 포함
print("-"*100)
print("python")

# 2. 문자 추출
#   - 인덱스를 통해서 문자 추출
#   - 인덱스 범위 벗어난 경우 오류(IndexError: string index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9])

#   -1 인덱스 (Reavese Index)
#   - 우측에서 좌측으로 인덱스
#   - 시작값 -1
print(lang[-1])
print(lang[-3])

#   3. 문자열 슬라이싱
#   - lang[3]: 문자 1개만 추출
#   - 부분 문자열을 추출하고 싶은 경우
msg = "python is all you need"
print(msg[0:6]) # 끝 인덱스+1
print(msg[:6])  # 시작 인덱스 생략 -> 자동 0 입력
print(msg[3:]) # 끝 인덱스 생략 -> 자동 -1 입력

print(msg[18:])
print(msg[-4:])
   # 4. 문자열 함수
   str = "hello world"

   print("="*100)
   # 4-1. len() : 문자열 길이 계산
   print(len(str))
   # 4-2. upper() and lower() : 대소문자 변경
   print(str.upper())
   print(str.lower())

   # 4-3, replace() : 문자열 내의 특정 문자 치환
   print(str.replace("h", "j" ))

   # 4-4 split(): 구분자를 기준으로 문자열 분할(Default: 공백)
   b = "hello world what a nice weather"
   print(b.split())
   print(b.split("w"))
   #4-5 strip(): 문자열의 좌우공백 제거
   id = "                  python1004"
   print(id)
   print(id.strip())
   id.lower()  "   cholong1004      "

#4-6, find() and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("0")) # Hell^o^ World
print(str.find("0")) # Hell w^o^orld
print(str.find("world")) # 못 찾으면 -1 출력
print(str.find("world")) # 단어의 첫 글자 인덱스
print(str.rfind("world")) # 단어의 첫 글자 인덱스

#4-7 Im(): 특정 문자열 포함하는지 확인(True, False 출력)
print("hi" in "hi")