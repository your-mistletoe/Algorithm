import sys

n = int(sys.stdin.readline())
arr = [0] * n

for i in range(n):
    arr[i] = int(sys.stdin.readline())

cnt = [0] * (max(arr) + 1)
              
arr = sorted(arr, key=lambda x:x)
print(*arr, end='\n')