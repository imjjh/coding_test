# 백준 스위치 문제
GENDER = 0
NUMBER = 1
BOY = 1
GIRL = 2

def toggle_switch(switch,n):
    if switches[n]==0:
        switches[n]=1
    else:
        switches[n]=0

# 스위치 갯수 입력
n= int(input())

# 스위치 입력 공백 구분
switches=list(map(int,input().split()))

# 학생 수 입력
len_stduent=int(input())

# 학생 수만큼 입력 받기 
steps=[]
for i in range(len_stduent):
    gender,num= map(int,input().split())
    steps.append((gender,num))

# 스위치 켜고 끄기

for step in steps:
    
    # 남자인 경우 
    if step[GENDER] == BOY:
        # 배수 반전
        for i in range(step[NUMBER]-1,n,step[NUMBER]):
            toggle_switch(switches,i)
    # 여자인 경우    
    else:
        # 넘버 자신 토글
        number = step[NUMBER]
        toggle_switch(switches,number-1)

        # 범위 이내일 때
        offset=1
        while 0 <= number-1 - offset < n and 0 <= number-1 + offset < n:

            if switches[number-1-offset] != switches[number-1+offset]:
                break

            toggle_switch(switches,number-1-offset)
            toggle_switch(switches,number-1+offset)

            offset+=1


for i in range(len(switches)):
    
    print(switches[i], end=" ")
    
    if (i+1) % 20 == 0:
        print()