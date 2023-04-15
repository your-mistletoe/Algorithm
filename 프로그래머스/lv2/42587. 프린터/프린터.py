from collections import deque
def solution(priorities, location):
    q = deque()
    cnt = 0
    
    for i, v in enumerate(priorities):
        q.append([i, v])
        
    while q:
        val = q.popleft()
        if any(val[1] < other[1] for other in q) :
            q.append(val)
        else:
            cnt += 1
            if val[0] == location:
                break
    return cnt
        
        