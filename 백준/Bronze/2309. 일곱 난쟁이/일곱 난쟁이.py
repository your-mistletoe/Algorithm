from itertools import permutations
arr = []
result = []

for i in range(9):
  arr.append(int(input()))

perm = list(permutations(arr, 7))
for j in perm:
  if sum(j) == 100:
    for rst in range(len(j)):
      result.append(j[rst])
      result.sort()
    break

for k in result:
  print(k)