from collections import Counter
def solution(k, tangerine):
    cnt = 0

    d = Counter(tangerine)
    
    sort_dic = sorted(list(d.items()), key=lambda x:x[1], reverse=True)

    for i, v in sort_dic:
        k -= v
        cnt += 1
        
        if k <= 0:
            break

    return cnt