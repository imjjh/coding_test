n,m=map(int,input().split())

arr=[]
visited=[False]*(n+1)

def dfs():
    if len(arr) == m:
        print(* arr)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            arr.append(i)

            dfs()

            arr.pop()
            visited[i]=False

dfs()