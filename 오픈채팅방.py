record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

answer = []
userdict = {}

for mes in record:
    if (mes.split(' ')[0] == 'Enter') | (mes.split(' ')[0] == 'Change'):
        userdict[mes.split(' ')[1]] = mes.split(' ')[2]

for mes in record:
    if mes.split(' ')[0] == 'Enter':
        answer.append("{}님이 들어왔습니다.".format(userdict[mes.split(' ')[1]]))
    elif mes.split(' ')[0] == 'Leave':
        answer.append("{}님이 나갔습니다.".format(userdict[mes.split(' ')[1]]))
    else:
         pass
print(answer)