# 9461

import sys

n=int(sys.stdin.readline())

test=[]

for i in range(n):
    test.append(int(sys.stdin.readline()))
    
dp=[0]*max(test)

# 초기값
dp[0:3]=[1,1,1]

for i in range(3,max(test)):
    dp[i]=dp[i-2]+dp[i-3]

for t in test:
    print(dp[t-1])