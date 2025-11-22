n,m=map(int,input().split())

arr=[]

def dfs():
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        # 내림차순 X # 배열의 크기가 0보다 클때, 마지막요소보다 작으면 continue
        if len(arr)>0 and arr[-1] > i:
            continue

        arr.append(i)
        dfs()
        arr.pop()

dfs()