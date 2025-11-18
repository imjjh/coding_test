import sys
import heapq

input=sys.stdin.readline
INF= int(1e9)

def dijkstra(start):
    # 힙 선언
    heap=[]

    # * 시작점 먼저 힙에 추가, 거리 갱신
    heapq.heappush(heap,(0,start))
    distances[start]=0

    # heap이 비어있지 않는 동안 반복
    while heap:
        # 최소 간선 꺼내기
        curr_distance, curr_node  = heapq.heappop(heap)
        
        # * heap에서 최소 간선을 꺼냈지만 알고 있던 거리보다 긴 경우 (버리기)
        if curr_distance > distances[curr_node]:
            continue

        # 현재 노드에서 갈 수 있는 간선들을 순회
        for next_distance, next_node  in graph[curr_node]:
            # 현재까지의 거리 + 다음 노드로 이동하는 거리 < 현재 알고있는 최소거리, 거리가 더 길 경우 방문하지 않음
            if curr_distance + next_distance  < distances[next_node]:
                # 최소거리 갱신
                distances[next_node] = curr_distance + next_distance
                heapq.heappush(heap,(distances[next_node],next_node))
                

v,e = map(int,(input().split()))

start= int(input())

graph=[[]for _ in range(v+1)] # 노드 번호와 인덱스를 동일 하게 쓰기 위해서 0은 쓰지 않음
distances=[INF]* (v+1) # 노드까지의 거리들을 무한대로 초기화
# 그래프 입력 (* 간선의 갯수 만큼)
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b)) # 최소힙과 순서를 동일하게 거리, 노드 순서로 입력


dijkstra(start)


# * 노드 0번은 존재하지 않으므로 생략
for i in range(1,len(distances)):
    if distances[i]==int(1e9):
        print("INF")
    else:
        print(distances[i])

