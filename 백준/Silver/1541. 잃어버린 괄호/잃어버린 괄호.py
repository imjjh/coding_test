# 1541

arr = list(input())

expression=[]
num=""

for ch in arr:
    if ch in "+-":
        expression.append(num)        
        expression.append(ch)
        num=""
    else:
        num+=ch

# 마지막 숫자 더하기
expression.append(num)

minus=False


result=int(expression[0])

for i in range(1,len(expression),2):
    # 첫 '-' 발견 이후부터는 전부 빼기 (그 이전은 양수 덧셈뿐)
    if expression[i] == '-':
        minus=True

    # 숫자 이면서 - 부호를 찾기 이전은 덧셈만
    if not minus:
        result+=int(expression[i+1])

    # 숫자이면서 - 부호를 찾은 이후는 뺼셈만
    if minus:
        result-=int(expression[i+1])


print(result)



