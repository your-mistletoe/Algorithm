n = int(input())
words = [0] * n
cnt = 0

for i in range(n):
    words[i] = input()

for word in words:
    # 알파벳 등장 여부 (a~z: 97~122)
    alphabet = [False] * 26
    # 입력된 단어의 맨 앞의 문자를 아스키코드 정수로 변환하여 인덱스 0부터 시작할 수 있게 -97해주고 True 할당
    # 리스트에 등장한 문자를 True, 등장하지 않았으면 False
    alphabet[ord(word[0])-97] = True
    for w in range(1, len(word)):
        # 앞뒤 문자가 같은 경우
        if word[w-1] == word[w]:
            continue
        # 앞뒤 문자가 다르고, 리스트 이미 등장했을 때
        elif word[w-1] != word[w] and alphabet[ord(word[w])-97] == True:
            cnt += 1
            break
        else: # alphabet[ord(word[w])] == False
            alphabet[ord(word[w])-97] = True

# 총 단어 갯수 - 그룹 단어가 아닌 개수
print(len(words) - cnt)