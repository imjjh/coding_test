n=int(input())

nums=list(map(int,input().split()))
dict={}
sorted_nums=sorted(list(set(nums)))


for i in range(len(sorted_nums)):
    dict[sorted_nums[i]]=i

for n in nums:
    print(dict[n],end=" ")
    