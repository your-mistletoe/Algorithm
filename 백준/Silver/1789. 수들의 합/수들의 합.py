s = int(input())
hap = 0
cnt = 0

for i in range(1, s+1):
  hap += i
  cnt += 1
  if hap > s:
    cnt -= 1
    break

print(cnt)