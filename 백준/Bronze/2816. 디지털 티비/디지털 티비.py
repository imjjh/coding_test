n=int(input())

channels=[]

for _ in range(n):
    channels.append(input())

k1= channels.index("KBS1")
k2= channels.index("KBS2")

if k1 > k2:
    k2+=1

print("1"*k1,end="")
print("4"*k1,end="")
print("1"*k2,end="")
print("4"*(k2-1),end="")

