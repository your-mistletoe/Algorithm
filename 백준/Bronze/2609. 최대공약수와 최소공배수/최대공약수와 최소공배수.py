a, b = map(int, input().split())

def gcd(a, b):
  if (a % b == 0):
    return b
  else:
    return gcd(b, a % b)

print(gcd(a, b), a * b // gcd(a, b), sep='\n')