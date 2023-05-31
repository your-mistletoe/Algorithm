def solution(s, skip, index):
    arr = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # skip을 순회
    for i in skip:
        # 알파벳 배열안에 skip의 요소가 있으면 요소값을 제거한 리스트를 생성
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
    # 암호 배열을 순회하며 결과 배열의 알파벳에 인덱스 값을 더한 값을 넣어준다. 
    for j in s:
        arr.append(alphabet[(alphabet.index(j)+index) % len(alphabet)])
        
    return ''.join(arr)