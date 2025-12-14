n,m= map(int,input().split())

countries=[]
ans=-1

for _ in range(n):
    country = list(map(int,input().split()))

    if country[0]==m:
        target=country

    countries.append(country)
    

sorted_arr=sorted(countries,key=lambda x: (-x[1], -x[2], -x[3]))

# 타겟과 동일한 메달수를 가진 첫번째 국가와 같은 등수를 가짐
for i in range(n):
    if sorted_arr[i][1:] == target[1:]:
        ans = i
        break

# 1 based
print(ans+1)