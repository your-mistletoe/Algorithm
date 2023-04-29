def solution(s):
    pivot = 0
    same = 0
    dif = 0
    arr = []
    for i, v in enumerate(s):
        if v == s[pivot]:
            same += 1
        else:
            dif += 1
            
        if same == dif:
            arr.append(s[pivot:i+1])
            if i < len(s)-1:
                pivot = i + 1
        else:
            if len(s) - i <  2:
                arr.append(s[pivot:len(s)-1])

    return len(arr)