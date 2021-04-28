import itertools

orders=["ABCFG", "AC", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
answer=[]

for num in course:
    total = {}
    for order in orders:
        if (num > len(order)):
            continue
        li = list(map(''.join, itertools.combinations(sorted(order), num)))
        for key in li:
            if key not in total:
                total[key] = 1
            else:
                total[key] += 1

    res = sorted(total.items(), key=lambda x: x[1], reverse=True)
    if (len(res) > 0):
        if (res[0][1] < 2):
            continue
        else:
            max_val = res[0][1]

        for i in range(len(res)):
            if (res[i][1] == max_val):
                answer.append(res[i][0])
            else:
                break
        else:
            continue

answer.sort()
print(answer)