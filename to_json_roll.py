import json

ar = []

with open('roll.txt', encoding='utf8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('roll.json', 'w', encoding='utf8') as e:
    json.dump(ar, e)
