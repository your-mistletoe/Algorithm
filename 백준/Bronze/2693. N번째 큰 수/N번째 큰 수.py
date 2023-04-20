n = int(input())
arr = []

for i in range(n):
  arr.append(list(map(int, input().split(' '))))

for j in arr:
  j.sort()
  print(j[-3])