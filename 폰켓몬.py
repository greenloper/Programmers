nums=[3,2,1,3]

answer = 0
length = len(nums) // 2
temp = list(set(nums))

for value in temp:
    if (answer < length):
        answer += 1

print(answer)