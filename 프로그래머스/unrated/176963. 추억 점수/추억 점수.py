def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    cnt = 0
    
    # 그리움 점수
    name_dict = dict(zip(name, yearning))
    
    for i in photo:
        cnt = 0
        for j in name_dict.keys():
            if j not in i:
                continue
            else:
                cnt += name_dict[j]
        answer.append(cnt)

    return answer