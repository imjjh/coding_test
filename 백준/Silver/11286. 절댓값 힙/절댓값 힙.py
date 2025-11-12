# 11286 절댓값 힙

import heapq
import sys

heap=[]
out=[]

n=int(input())

for i in range(n):

    num=int(input())


    # 0 입력
    if num == 0:
        # 비어있는 경우 
        if len(heap)==0:
            value=0
        # 값이 있는 경우
        else:
            value = heapq.heappop(heap)[1]

        out.append(str(value))

    else:

        heapq.heappush(heap,(abs(num),num))

sys.stdout.write("\n".join(out))