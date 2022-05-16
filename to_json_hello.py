import json

ar = []

with open('hello.txt', encoding='utf8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('hello.json', 'w', encoding='utf8') as e:
    json.dump(ar, e)
