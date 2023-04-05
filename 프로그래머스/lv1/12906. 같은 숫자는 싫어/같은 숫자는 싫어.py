def solution(arr):
    answer = []
    
    target = -1
    for i in arr:
        if i != target:
            answer.append(i)
        target = i
    return answer