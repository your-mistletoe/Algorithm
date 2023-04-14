def solution(k, score):
    q = []
    result = []
    
    for i in range(len(score)):
        q.append(score[i])
        if i < k:
            result.append(min(q))
        else:
            q.sort()
            result.append(q[-k])
    
    return result