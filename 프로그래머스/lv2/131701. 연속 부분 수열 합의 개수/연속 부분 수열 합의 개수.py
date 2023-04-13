def solution(elements):
    result = set()
    e = elements * 2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            result.add(sum(e[j:j+i+1]))

    return len(result)