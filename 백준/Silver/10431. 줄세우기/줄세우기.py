n=int(input())

for i in range(n):
    line=list(map(int,input().split()))
    line=line[1:]

    ans=0
    for j in range(20):
        line_before= line[:j]
        for k in range(len(line_before)):
            if line[j] < line[k]:
                ans+=1

    print(i+1, ans)