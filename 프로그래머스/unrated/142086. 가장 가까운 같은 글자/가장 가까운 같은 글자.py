def solution(s):
    result = []
    words = {}

    for i, v in enumerate(s):
        if v not in words.keys():
            words[v] = i    
            result.append(-1)
        else:
            result.append(i-words[v])
            words[v] = i
        
    return result
    
        