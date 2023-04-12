from itertools import combinations
def solution(number):
    cnt = 0
    com = combinations(number, 3)
    for i in list(com):
        if sum(i) == 0:
            cnt += 1
    return cnt