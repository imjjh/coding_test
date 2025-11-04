import sys


def solution(start_row,start_col,end_row,end_col,r,c):
    extent = (end_row-start_row)*(end_col-start_col)

    if extent == 1:
        return 1

    center_col = (end_col+start_col) // 2
    center_row = (end_row+start_row) // 2
    
    # Z 이동에서 첫번째 영역에 속한 경우
    if center_row >= r and center_col >= c:
        return solution(start_row,start_col,center_row,center_col,r,c)
    # 두번째 영역
    elif center_row >= r and center_col < c:
        return solution(start_row,center_col,center_row,end_col,r,c) + int(extent * (1/4))
    # 세번째 영역
    elif center_row < r and center_col >= c:
        return solution(center_row,start_col,end_row,center_col,r,c) + int(extent * (2/4))
    # 네번쨰 영역
    elif center_row < r and center_col < c:
        return solution(center_row,center_col,end_row,end_col,r,c) + int(extent * (3/4))
    
    

N,r,c=map(int,sys.stdin.readline().split())



# Z 분할 정복, 재귀
# 2^N * 2^N

# N이 1씩 커질때마다 양이 4배로 늘어감(길이는 가로,세로 각각 2배씩)

# 한변의 길이 계산
length = 2**N

# 1부터 시작이므로 0행 0열 부터 시작으므로 r+1, c+1 # 넓이처럼 풀었지만 실제로는 방문순서이기에 0번쨰 방문부터 시작이므로 결과-1를 출력
print(solution(0,0,length,length,r+1,c+1)-1)


