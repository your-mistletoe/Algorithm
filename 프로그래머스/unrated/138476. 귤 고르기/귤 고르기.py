from collections import Counter
def solution(k, tangerine):
    dic = {}
    q = []
    cnt = 0

    # for i in tangerine:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1

    d = Counter(tangerine)
    # sort_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    sort_dic = sorted(list(d.items()), key=lambda x:x[1], reverse=True)

    for i, v in sort_dic:
        k -= v
        cnt += 1
        
        if k <= 0:
            break
        

    return cnt