import math

H,W,N,M=map(int,input().split())


# 행 최대 인원
max_row= math.ceil((H / (N+1)))

# 열 최대 인원
max_col = math.ceil((W / (M+1)))

# print(max_row, max_col)
print(max_row * max_col)
