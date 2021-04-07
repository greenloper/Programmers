s="abcde"

l=len(s)
if l%2==0:
    l=(l-2)/2
else:
    l=(l-1)/2
print(s[int(l):-int(l)])