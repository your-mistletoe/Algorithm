arr = []
result = []
total = 0

for _ in range(10):
  arr.append(list(map(int, input().split())))

for o, i in arr:
  total += i
  total -= o
  result.append(total)

print(max(result))