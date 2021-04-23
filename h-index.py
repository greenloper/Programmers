citations=[3,0,6,1,5]

citations.sort(reverse=True)
answer = max(map(min, enumerate(citations, start=1)))
print(answer)