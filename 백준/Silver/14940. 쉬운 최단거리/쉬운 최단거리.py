from collections import deque


ROW,COL,DISTANCE=0,1,2

def bfs(board,n,m):
    # 2 (목적지 탐색) 탐색
    def find_dst():
        for i in range(n):
            for j in range(m):
                if board[i][j]==2:
                    return i,j
                
    direction=((-1,0),(1,0),(0,-1),(0,1))
    visited=[[False]*m for _ in range(n)] # 방문 여부
    distance=[[0]*m for _ in range(n)] # 거리를 표시할 리스트
    
    dst=find_dst()


    # 목적지의 행, 열, 거리
    queue=deque([(dst[ROW],dst[COL],0)])
    visited[dst[ROW]][dst[COL]]=True #방문처리

    while queue:
        node = queue.popleft() # 꺼내기
        
        # 상하좌우에 대해 방문
        for dir in direction:
            # 상하좌우 좌표 계산
            next_row= node[ROW]+dir[0]
            next_col= node[COL]+dir[1]

            # 좌표가 유효 & 방문한적 없음 & 갈수없는 곳 (0)이 아님
            if (0<=next_row<n and 0<=next_col<m) and (not visited[next_row][next_col]) and (board[next_row][next_col] != 0):
                # 큐에 추가 (행, 열, 현재 거리 + 1)
                queue.append((next_row,next_col,node[DISTANCE]+1))
                visited[next_row][next_col]=True #방문처리
                # 좌표에 내용 반영
                distance[next_row][next_col]=node[DISTANCE]+1


    # 원래 갈수있는 땅(1)이지만 도달할 수 없이 거리가 0인 것을 -1로 변경
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and distance[i][j]==0:
                distance[i][j] = -1
    return distance
        
    
n,m=map(int,input().split())

board=[] # 실제 지도



for _ in range(n):
    board.append(list(map(int,input().split())))


distance=bfs(board,n,m)

for i in range(n):
    for j in range(m):
        print(distance[i][j],end=" ")
    print()