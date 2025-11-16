n,target=list(map(int,input().split()))

coins=[]

dp=[-1]*(target+1)

for i in range(n):
    coin = int(input())
    
    if target < coin:
        continue
    
    coins.append(coin)
    dp[coin]=1 # 동전이 있는 경우엔 초기값을 1로 설정


if len(coins)>0:
    for i in range(min(coins),target+1):
        
        for coin in coins:

            # 범위 밖인 경우
            if i - coin < 0:
                continue

            # 코인의 값을 더하기 이전 만들수 있는 값인지 검사
            if dp[i-coin]  != -1:
                # 코인의 최소 값이 없는 경우 (값이 -1인 경우)
                if dp[i]== -1:
                    dp[i] = dp[i-coin] + 1

                # 코인의 최소 값이 있는 경우
                else:
                    dp[i]=min(dp[i-coin]+1,dp[i])

print(dp[target])