from math import sqrt
def solution(number, limit, power):
    person = [0] * number
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(sqrt(i)) + 1):
            if i % j == 0:
                cnt += 1
                if (j != (i // j)):
                    cnt += 1
        if cnt > limit:
            cnt = power
        person[i-1] = cnt
    return sum(person)
        