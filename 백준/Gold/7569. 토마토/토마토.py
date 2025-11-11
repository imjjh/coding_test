from collections import deque
import sys


def bfs(width,length,height,box,multi_sources):
    queue=deque(multi_sources)
    days=0
    while queue:
        curr_h,curr_n,curr_m,curr_depth=queue.popleft()
        
        for m,n,h in directions:
            next_m=curr_m+m
            next_n=curr_n+n
            next_h=curr_h+h
        
            # 범위 이내 and 안익은 토마토?
            if (0 <= next_m < width and 0 <= next_n < length and 0 <= next_h <height)\
                 and box[next_h][next_n][next_m]==0:

                # 익히기
                box[next_h][next_n][next_m] = 1
                queue.append((next_h,next_n,next_m,curr_depth+1))
                days=curr_depth+1
    
    return days

def check_unripe(box):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if (box[i][j][k]==0):
                    return True
                    

m,n,h =map(int,(sys.stdin.readline().split()))

box=[]

directions=((0,0,1),
            (0,0,-1),
            (0,1,0),
            (0,-1,0),
            (1,0,0),
            (-1,0,0))

for i in range(h):
    layer=[]
    for j in range(n):
        layer.append(list(map(int,sys.stdin.readline().split())))
    box.append(layer)



already_ripe_tomatoes=[]
    
# 이미 익은 토마토 정리
for i in range(h):
    for j in range(n):
        for k in range(m):
            if (box[i][j][k]==1):
                already_ripe_tomatoes.append((i,j,k,0))

result=bfs(m,n,h,box,already_ripe_tomatoes)


if (check_unripe(box)):
    print(-1)
else:
    print(result)

                