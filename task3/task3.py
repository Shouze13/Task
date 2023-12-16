import json
import sys

t = sys.argv[1]
v = sys.argv[2]
with open(t, 'r') as test:
    test.data = json.load(test)

with open(v, 'r') as values:
    values.data = json.load(values)

def binar(t,k):
    low = 0
    high = len(t)-1

    while high >= low:
        mid = (high+low)//2
        guess = t[mid]['id']
        if guess == k:
            return t[mid]['value']
        if guess > k:
            high = mid - 1
        else:
            low = mid + 1

def rekur(m):
    for i in m:
        if 'value' in i:
            k = i.get('id')
            i['value'] = binar(values.data['values'], k)
            print('\n')
        if 'values' in i:
            rekur(i['values'])
    return test.data

t = rekur(test.data['tests'])

with open('report.json', 'w') as file:
    json.dump(t, file, indent=1)
