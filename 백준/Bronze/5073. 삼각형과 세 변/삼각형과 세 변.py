while True:
    triangle = list(map(int,input().split()))

    if sum(triangle)==0:
        break

    triangle.sort()

    if triangle[0]+ triangle[1] <= triangle[2]:
        print("Invalid")
        continue

    triangle = set(triangle)

    if len(triangle)==1:
        print("Equilateral")

    elif len(triangle)==2:
        print("Isosceles")

    else:
        print("Scalene")
