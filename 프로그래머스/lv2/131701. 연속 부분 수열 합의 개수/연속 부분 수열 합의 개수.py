def solution(elements):
    result = set()

    for i in range(len(elements)):
        value = elements[i]
        result.add(value)
        for j in range(i+1, i+len(elements)):
            value += elements[j % len(elements)]
            result.add(value)
    return len(result)   