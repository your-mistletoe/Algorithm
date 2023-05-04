def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    
    for i, v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            result[stack.pop()] = v
        stack.append(i)
    return result

