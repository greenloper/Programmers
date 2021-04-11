s="pPoooyY"

answer = True
p = 0
y = 0

for i in s:
    if i in ["p", "P"]:
        p += 1
    elif i in ["y", "Y"]:
        y += 1

if p == y:
    print("True")
else:
    print("False")