n = int(input())
arr = [0] * n
stack = []
command = ['push', 'pop', 'size', 'empty', 'top']

for i in range(n):
    arr[i] = input()

for j in arr:
    if len(j) > 5:
        c, v = j.split(' ')
        if c == command[0]:
            stack.append(v)
    elif j == command[1]:
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif j == command[2]:
        print(len(stack))
    elif j == command[3]:
        if stack:
            print('0')
        else:
            print('1')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')