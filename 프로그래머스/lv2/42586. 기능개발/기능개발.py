def solution(p, s):
    result = []
    cnt = 0
    day = 0
    
    while p:
        if p[0] + s[0] * day >= 100:
            p.pop(0)
            s.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
                cnt = 0
            day += 1
        
    result.append(cnt)
    
    return result