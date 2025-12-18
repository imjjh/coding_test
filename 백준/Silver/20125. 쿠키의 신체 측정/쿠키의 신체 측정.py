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


n=int(input())


plate=[]


for _ in range(n):
    plate.append(list(input()))

heart_row, heart_col=find_heart(n)


# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
left_arm=0
right_arm=0
waist=0
left_leg=0
right_leg=0


# 왼쪽 팔 찾기
next_col=heart_col-1

while is_valid(n,heart_row,next_col):
    
    if plate[heart_row][next_col]!='*':
        break

    left_arm+=1
    next_col-=1


# 오른 팔 찾기
next_col=heart_col+1

while is_valid(n,heart_row,next_col):
    
    if plate[heart_row][next_col]!='*':
        break

    right_arm+=1
    next_col+=1


# 허리 찾기
next_row=heart_row+1

while is_valid(n,next_row,heart_col):
    
    if plate[next_row][heart_col]!='*':
        break

    waist+=1
    next_row+=1

# 왼쪽 다리 찾기
next_row = heart_row + waist + 1
left_leg_col = heart_col - 1

while is_valid(n,next_row,left_leg_col):

    if plate[next_row][left_leg_col]!='*':
        break

    left_leg+=1
    next_row+=1



# 오른 다리 찾기
next_row = heart_row + waist + 1
right_leg_col = heart_col + 1

while is_valid(n,next_row,right_leg_col):

    if plate[next_row][right_leg_col]!='*':
        break

    right_leg+=1
    next_row+=1

    

# 1 based
print(heart_row+1,heart_col+1)

print(left_arm,end=" ")
print(right_arm,end=" ")
print(waist,end=" ")
print(left_leg,end=" ")
print(right_leg,end=" ")