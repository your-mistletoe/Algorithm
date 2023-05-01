n = int(input())
cnt = 0

if n < 10:
  print(n)
elif n < 100:
  print(n)
else:
  for i in range(n, 100, -1):
    if (i // 100 - i % 100 // 10) == (i % 100 // 10 - i % 100 % 10):
      cnt += 1
  cnt += 99
  print(cnt)