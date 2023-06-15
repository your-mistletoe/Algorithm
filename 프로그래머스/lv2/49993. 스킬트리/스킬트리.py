def solution(skill, skill_trees):
    rst = 0
    for s in skill_trees:
        idx = 0
        rst1, rst2 = 0, 0
        for i in range(len(s)):
            print(s[i])
            if s[i] in list(skill):
                rst1 += 1
            if idx >= len(skill):
                break
            if skill[idx] == s[i]:
                idx += 1
                rst2 += 1
        if rst1 == rst2:
            rst += 1
    return rst
