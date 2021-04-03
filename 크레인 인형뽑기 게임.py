board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

bucket=[]
answer=[]

for m in moves:
    for i in range(len(board)):
        if board[i][m-1]>0:
            bucket.append(board[i][m-1])
            board[i][m-1]=0
            if bucket[-1:]==bucket[-2:-1]:
                answer+=bucket[-1:]
                bucket=bucket[:-2]
            break

print(len(answer)*2)