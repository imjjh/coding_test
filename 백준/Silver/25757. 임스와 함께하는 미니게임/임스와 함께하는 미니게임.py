import sys


n,selected_game= sys.stdin.readline().split()


games={'Y':2,'F':3,'O':4}

names=set()

for _ in range(int(n)):
    names.add(sys.stdin.readline())


print(len(names)//(games[selected_game]-1))


