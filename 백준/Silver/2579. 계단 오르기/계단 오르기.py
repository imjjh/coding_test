import sys

n=int(sys.stdin.readline())

stairs=[]

for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

# 계단 수 1
if n==1:
    print(stairs[0])
# 계단 수 2
elif n==2:
    print(stairs[0]+stairs[1])
# 계단 수 3 이상
else:

    d=[0]*n # DP
    # 기저값 정의
    d[0]= stairs[0]
    d[1]= stairs[0] + stairs[1]
    d[2]= max(stairs[0]+stairs[2],+stairs[1]+stairs[2])


    for i in range(3,n):
        d[i]= d[i-3]+stairs[i-1]+stairs[i] # 2칸 이후 1칸 이동하는 경우
        d[i] = max(d[i-2] + stairs[i],d[i]) # 2칸 이동 하는 경우

    print(d[-1]) 