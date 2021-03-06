dartResult="1S2D*3T"
answer=0

bonus = {'S' : 1, 'D' : 2, 'T' : 3}
option = {'*' : 2, '#' : -1}

a = [0,0,0]
flag = -1

for idx, dart in enumerate(dartResult) :
    if dart.isdigit() :
        flag += 1
        if dart == '0' :
            continue
        elif dartResult[idx+1].isdigit() :
            a[flag] = int(dart)*10
            flag -= 1
        else :
            a[flag] = int(dart)

    elif dart in 'SDT':
        a[flag] **= bonus[dart]

    else :
        if dart == "*" :
            a[flag-1] *= 2

        a[flag] *= option[dart]

print(sum(a))