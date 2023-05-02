while True:
  s = 0
  arr = []
  n = int(input())
  if n == -1:
    break

  for i in range(1, n // 2 + 1):
    if n % i == 0:
      s += i
      arr.append(i)

  if s == n:
    print(f"{n} = ", end='')
    for j in range(len(arr)):
      if j == len(arr)-1:
        print(arr[j])
      else:
        print(arr[j], end=' + ')
  else:
    print(f"{n} is NOT perfect.")