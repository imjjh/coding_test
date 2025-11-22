n,m=map(int,input().split())

visited=[False]*(n+1)
arr=[]

def dfs():
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        # 배열의 길이가 0보다 크고, arr의 맨 마지막 요소보다 값이 작은 경우 continue
        if len(arr) > 0 and arr[-1] > i:
            continue

        if not visited[i]:
            visited[i]=True
            arr.append(i)
            dfs()
            visited[i]=False
            arr.pop()

dfs()