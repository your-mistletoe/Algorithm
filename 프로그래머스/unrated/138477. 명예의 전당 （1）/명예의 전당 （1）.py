def solution(k, score):
    q = []
    result = []
    
    for i in score:
        q.append(i)
        if len(q) > k:
            q.remove(min(q))        
        result.append(min(q))
    
    return result