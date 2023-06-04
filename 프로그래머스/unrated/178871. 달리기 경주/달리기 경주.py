def solution(players, callings):
    # 선수(key) 딕셔너리, 순위(key) 딕셔너리
    players_dic = {i:v for i, v in enumerate(players)}
    rank_dic = {v:i for i, v in enumerate(players)}

    for i in callings:
        current_player = players_dic[rank_dic[i]]
        front_player = players_dic[rank_dic[i]-1]
        
        current_rank = rank_dic[current_player]
        front_rank = rank_dic[front_player]
        
        players_dic[current_rank], players_dic[front_rank] = players_dic[front_rank], players_dic[current_rank]
        rank_dic[current_player], rank_dic[front_player] = rank_dic[front_player], rank_dic[current_player]
    
    return list(players_dic.values())
        
            