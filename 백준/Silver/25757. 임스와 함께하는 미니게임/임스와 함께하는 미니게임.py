n,selected_game= input().split()


games={'Y':2,'F':3,'O':4}

names=set()

for _ in range(int(n)):
    names.add(input())


print(len(names)//(games[selected_game]-1))


