a = input('Enter any characters: ')
b = {i:a.count(i) for i in a}
print(b)

d = list(b.values())
print(d)

s = {i:d.count(i) for i in d}
print(s)

if len(s.keys())>2 or (max(s.keys())-min(s.keys())>1):
    print('It\'s not my string')
elif max(s.keys())>=2 and (min(s.keys())+1)==max(s.keys()):
    print('It\'s not my string')
else:
    print('My String')


