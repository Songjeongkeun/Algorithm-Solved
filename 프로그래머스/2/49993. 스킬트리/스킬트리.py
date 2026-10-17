def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = ''
        
        for s in tree:
            if s in skill:
                temp += s
        if temp == skill[:len(temp)]:
            answer += 1
            
    return answer