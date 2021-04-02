new_id="abcdefghijklmn.p"
new_id=list(new_id)
word=["-", "_", "."]

#1단계
for i in range(0, len(new_id)):
    if (new_id[i]>="A") and (new_id[i]<="Z"):
        new_id[i]=new_id[i].lower()

#2단계
copy_new_id=[]
for i in range(0, len(new_id)):
    if (new_id[i]>="a" and new_id[i]<="z") or (new_id[i]>="0" and new_id[i]<="9") or (new_id[i] in word):
        copy_new_id.append(new_id[i])
new_id=copy_new_id[:]

#3단계
copy_new_id=[]
for i in range(0, len(new_id)):
    if new_id[i]==".":
        if (i<len(new_id)-1) and new_id[i+1]==".":
            i+=1
        elif (i<len(new_id)-1) and new_id[i+1]!=".":
            copy_new_id.append(".")
    else: copy_new_id.append(new_id[i])
new_id=copy_new_id[:]

#4단계
if len(new_id)>=1:
    if new_id[0]==".":
        del new_id[0]
    if new_id[-1]==".":
        del new_id[-1]

#5단계
if len(new_id)==0:
    new_id.append("a")

#6단계
if len(new_id)>=16:
    new_id=new_id[0:15]
    if new_id[-1]==".":
        del new_id[-1]

#7단계
if len(new_id)<=2:
    while(len(new_id)<3):
        new_id.append(new_id[-1])

print("".join(new_id))
