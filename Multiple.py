# [문제]
# 3과 5의 배수 숫자의 합 구하기
# 1~10 사이의 3과 5의 배수는 3, 5, 6, 9입니다.
# 이들의 합은 23입니다. 1~1000 사이의 3과 5의 배수 합을 구하세요.
number = 1000
number3=[]
number5=[]
number15=[]
for i in range(0,number,3):
    number3.append(i)
for i in range(0,number,5):
    number5.append(i)
for i in range(0,number,15):
    number15.append(i)
print(sum(number3)+sum(number5)-sum(number15))

    
