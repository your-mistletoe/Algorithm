def solution(a, b, n):
    sum = 0
    while n >= a:
        remain = n % a
        plus = (n // a) * b
        
        sum += plus
        n = plus + remain
    return sum