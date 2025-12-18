import sys

def find_heart(n):
    # 머리 찾기 & 심장 찾기
    for i in range(n):
        for j in range(n):
            # 머리는 항상 가장 위에 있음
            if plate[i][j] == '*':
                # 머리(row) + 1 == 심장(row) 
                return (i+1,j)


def is_valid(len_plate,curr_row,curr_col):
    return (0 <= curr_row < len_plate) and (0<= curr_col <len_plate)


def get_length(n,r,c,dr,dc):
    length=0
    curr_r=r
    curr_c=c
    while (0 <= curr_r < n) and (0 <= curr_c < n) and plate[curr_r][curr_c]=="*":
        length+=1
        curr_r+=dr
        curr_c+=dc 
    
    return length



n=int(sys.stdin.readline().rstrip())


plate=[]


for _ in range(n):
    plate.append(list(sys.stdin.readline().rstrip()))

heart_row, heart_col=find_heart(n)


# 왼쪽 팔 찾기
left_arm= get_length(n,heart_row,heart_col-1,0,-1)
# 오른 팔 찾기
right_arm= get_length(n,heart_row,heart_col+1,0,1)
# 허리 찾기
waist=get_length(n,heart_row+1,heart_col,1,0)
# 왼쪽 다리 찾기
left_leg=get_length(n,heart_row + waist + 1,heart_col - 1,1,0)
# 오른 다리 찾기
right_leg=get_length(n,heart_row + waist + 1,heart_col + 1,1,0)
    

# 1 based heart
print(heart_row+1,heart_col+1)

print(left_arm,end=" ")
print(right_arm,end=" ")
print(waist,end=" ")
print(left_leg,end=" ")
print(right_leg,end=" ")