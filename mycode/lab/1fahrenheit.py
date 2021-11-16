print("섭씨 온도를 입력하시면 화씨로 바꿔드립니다")
cir = input()
print(cir+"도를 입력하셨습니다.")

# 입력한 문자열을 숫자로 변경하여 연산
cir_temp=float(cir)
har_temp=((9/5)*cir_temp)+32

# 연산결과를 프린트
print("섭씨온도 : ",cir_temp)
print("화씨온도 : ",har_temp)
