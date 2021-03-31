skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]

answer=0

for skills in skill_trees:
    skill_list=list(skill)

    for s in skills:
        if s in skill:
            if s!=skill_list.pop(0):
                break
    else:
        answer+=1

print(answer)