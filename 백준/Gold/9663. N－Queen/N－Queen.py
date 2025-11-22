n=int(input())


def solve(n):
    col=set() # c
    diag=set() # r + c
    anti=set() # r - c

    def dfs(r):
        cnt=0
        # 마지막 행까지 배치 완료한 경우
        if r==n:
            return 1
        
        # 열 탐색
        for c in range(n):
            # 놓을 수 없는 위치인 경우
            d=r+c
            a=r-c
            if (c in col) or (d in diag) or (a in anti):
                continue
            
            col.add(c)
            diag.add(d)
            anti.add(a)
            cnt+=dfs(r+1) # 놓을 수 있는 경우, 다음행 탐색
            col.remove(c)
            diag.remove(d)
            anti.remove(a)

        return cnt

    return dfs(0)
    
print(solve(n))