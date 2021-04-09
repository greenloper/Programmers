n=45
answer=[]
while True:
    n, rest=divmod(n, 3)
    answer.append(rest)
    if n==0:
        break
print(sum([i*3**idx for idx, i in enumerate(reversed(answer))]))