N=5
stages=[2,1,2,6,2,4,3,3]
result={}

denominator=len(stages)
for stage in range(1, N+1):
    if denominator!=0:
        count=stages.count(stage)
        result[stage]=count/denominator
        denominator-=count
    else:
        result[stage]=0

print(sorted(result, key=lambda x : result[x], reverse=True))