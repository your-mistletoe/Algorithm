n, k = map(int, input().split())
arr = []
q = 1

while q <= n:
  if n % q == 0:
    arr.append(n // q)
  q += 1

if len(arr) < k:
  print(0)
else:
  print(arr[-k])