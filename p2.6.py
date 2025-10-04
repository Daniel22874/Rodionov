a = int(input())
b = int(input())
c = int(input())
m = -20
n = -10
D = (b ** 2) - (4 * a * c)
print(D)
if D > 0:
    x1 = ((-1) * b - (D ** 0.5)) / (2 * a)
    x2 = ((-1) * b + (D ** 0.5)) / (2 * a)
    print(x1, x2)
    if (x1 >= m and x1 <= n) or (x2 >= m and x2 <= n):
        print('Решение попадает в отрезок')
    else:
        print('Решение не попадает в отрезок')
if D == 0:
    x = -b / (2 * a)
    print(x)
    if x >= m and x <= n:
        print('Решение попадает в отрезок')
    else:
        print('Решение не попадает в отрезок')
