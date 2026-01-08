# 크로스 컨트리 9017
MAX_TEAM_NUMBER=201 # 0 based
out=[]

n=int(input())

for i in range(n):
    count=[0]*MAX_TEAM_NUMBER
    scores=[0]*MAX_TEAM_NUMBER
    calculated=[0]*MAX_TEAM_NUMBER

    len_players=int(input())
    players=list(map(int,input().split()))

    # 각 팀의 몇명의 선수가 있는지 체크
    for player in players:
        count[player]+=1
    
    # 등수별로 점수 매기기
    rank_score=1

    for j in range(len_players):
        if count[players[j]] < 6:
            continue
        # 4명만 더하기
        if calculated[players[j]] < 4:
            scores[players[j]]+=rank_score
            calculated[players[j]]+=1
        rank_score+=1
    
    # 참가하지 않은 팀들은 INF로 수정
    for j in range(MAX_TEAM_NUMBER):
        if scores[j]==0:
            scores[j]=float("INF")
    

    # 가장 낮은 점수 (우승 후보 찾기)
    winner_candidate_score=min(scores)
    len_winner_candidate = scores.count(winner_candidate_score)

    if len_winner_candidate == 1:
        winner = scores.index(winner_candidate_score)
        out.append(winner)
        continue

    # 우승 후보팀들이 몇번팀인지 찾기
    winner_candidates=[]
    for j in range(MAX_TEAM_NUMBER):
        if scores[j] == winner_candidate_score:
            winner_candidates.append(j)

    # 우승 후보팀 중 5번째 주자가 가장 빨리 들어온 팀 찾기

    count=[0]*MAX_TEAM_NUMBER  # 다시 카운트를 위한 초기화

    for j in range(len_players):
        # 우승 후보가 아니면 스킵
        if players[j] not in winner_candidates:
            continue
        
        count[players[j]]+=1

        # 가장 먼저 5명이 들어온 경우
        if count[players[j]]==5:
            winner=players[j]
            break
    

    out.append(winner)


print("\n".join(map(str,out)))


