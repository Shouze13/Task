import sys
count = 0
file_path_circle = sys.argv[1]
file_path_points = sys.argv[2]

with open(file_path_circle) as circle:
    circ = [i.split() for i in circle]

with open(file_path_points) as point:
    pnt = [u.rstrip() for u in point]
    p = [p.split() for p in pnt]

for x_0, y_0, r in zip(circ[0][0], circ[0][1], circ[1]):
    x_0, y_0, r = map(float, [x_0, y_0, r])

for i in p:
    if count >= 100:
        break
    x, y = map(float, [i[0], i[1]])
    point = pow(x - x_0, 2) + pow(y - y_0, 2)
    R = r ** 2
    if point == R:
        print('0', "\n")
    elif point < R:
        print('1', "\n")
    else:
        print('2', "\n")
    count += 1
