from itertools import permutations
arr = []

def solution(numbers):
    for i1, i2 in permutations(numbers, 2):
        if i1 + i2 not in arr:
            arr.append(i1 + i2)
    
    arr.sort()

    return arr