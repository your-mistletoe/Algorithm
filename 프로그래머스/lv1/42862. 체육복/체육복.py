def solution(n, lost, reserve):
    result = 0
    lost.sort()
    reserve.sort()
    n_reserve = [r for r in reserve if r not in lost]
    n_lost = [l for l in lost if l not in reserve]
    
    for r in n_reserve:
        prev = r-1
        nex = r+1
        if prev in n_lost:
            n_lost.remove(prev)
        elif nex in n_lost:
            n_lost.remove(nex)
    
    result = n - len(n_lost)
    return result

