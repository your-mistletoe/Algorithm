from collections import deque
def solution(s):
    # '('가 오면 result.append() 
    # ')'가 오면 cnt > 0 일 때 result.pop(), cnt -= 1
    
    result = []
    cnt = 0
    
    for i in s:
        if i == '(':
            result.append(i)
            cnt += 1
        else:
            if cnt > 0:
                result.pop()
                cnt -= 1
                continue
            return False
    
    if len(result) == 0:
        return True
    
    return False
        
    