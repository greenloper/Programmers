from collections import deque

priorities=[2,1,3,2]
location=2
answer=0

d=deque([(v,i) for i, v in enumerate(priorities)])

while len(d):
    item=d.popleft()
    if d and max(d)[0]>item[0]:
        d.append(item)
    else:
        answer+=1
        if item[1]==location:
            break

print(answer)