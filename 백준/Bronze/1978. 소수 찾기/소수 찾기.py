n = int(input())
arr = map(int, input().split())
cnt = 0

for i in arr:
  sosu = 0
  if i > 1:
    for j in range(2, i):
      # 소수
      if i % j == 0:
        sosu += 1
    if sosu == 0:
      cnt += 1

print(cnt)