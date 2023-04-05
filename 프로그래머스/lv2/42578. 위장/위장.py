def solution(clothes):
    answer = 1
    closet = {}
    
    for i, c in clothes:
        if c not in closet:
            closet[c] = []
        closet[c].append(i)
    
    for key in closet.keys():
        answer *= len(closet[key]) + 1
        
    return answer - 1