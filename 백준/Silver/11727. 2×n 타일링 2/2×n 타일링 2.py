n=int(input())

dp=[0]*n    

dp[0:2]=[1,3]

for i in range(2,n):
    dp[i]=dp[i-1]+ dp[i-2]*2

print(dp[n-1]%10007)