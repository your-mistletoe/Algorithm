import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    number = n // h + 1
    if n % h == 0:
        floor = h
        number = number - 1
    print(floor*100+number)