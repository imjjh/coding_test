# 11286 절댓값 힙

import heapq

plus=[]
minus=[]

n=int(input())

for i in range(n):

    num=int(input())

    # 0 입력
    if num == 0:
        # 둘다 비어있는 경우 
        if len(plus)==0 and len(minus)==0:
            v=0

        # 한쪽만 비어있는 경우?
        elif len(plus)==0:
            v= - (heapq.heappop(minus))

        # 한쪽만 비어있는 경우?
        elif len(minus)==0:
            v = heapq.heappop(plus)
        # 양쪽 모두 값 존재
        else:
            # 절댓값이 작은 수를 찾기 위해 최상단을 비교 # 같은 경우 -부터 출력
            if plus[0] >= minus[0]:
                v = - ( heapq.heappop(minus)) 
            else:
                v = heapq.heappop(plus)
        
        print(v)
            
    else:

        # 0 미만 # 부호 반대로 + 로 저장 (파이썬 모듈은 최솟값만 지원함, 절댓값 최소를 찾기위해 부호 반전)
        if num < 0 :
            num *= -1
            heapq.heappush(minus,num)

        # 0 이상
        else:
            heapq.heappush(plus,num)

        
