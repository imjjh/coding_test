taesoo_index=-1
rank=-1
scores=[]

n,taesoo,p= map(int,input().split())

if 0 < n:
    scores.extend(map(int,input().split()))

scores.append(taesoo)

sorted_scores=sorted(scores,reverse=True)

for i in range(len(sorted_scores)):
    if sorted_scores[i]==taesoo:
        if rank == -1:
            rank = i

        taesoo_index=i

if not (taesoo_index + 1 <= p): # 1 based
    print(-1)
else:
    print(rank+1) # 1based
