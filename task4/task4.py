import sys
file_path = sys.argv[1]
d = []
with open(file_path) as numer:
    n = [int(n.rstrip()) for n in numer]

for j in n:
    i = 0
    delta = 0
    while i <= len(n) - 1:
        delta += abs(j - n[i])
        i += 1
    d.append(delta)

d = min(d)
print(d) #Минимальное количество ходов



