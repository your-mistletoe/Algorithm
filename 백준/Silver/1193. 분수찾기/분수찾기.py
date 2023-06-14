import sys

t = int(sys.stdin.readline())

sum = 0
zigzag = 0

while sum < t:
    zigzag += 1
    sum += zigzag

num = sum - t

if zigzag % 2 == 0:
    분자 = zigzag - num
    분모 = zigzag + 1 - 분자
else:
    분모 = zigzag - num
    분자 = zigzag + 1 - 분모

print(f'{분자}/{분모}')
