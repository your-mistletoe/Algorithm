t = int(input())
arr = []

for i in range(t):
  n = int(input())
  binary = bin(n)
  arr.append(binary[2:])
  for i, v in enumerate(reversed(arr[i])):
    if '1' in v:
      print(i)