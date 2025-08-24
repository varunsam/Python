'''
    day of the week
'''

d,m,Y = 22, 8, 2025

c, y = Y // 100, Y % 100
sm = m - 2 if m > 2 else m + 10
y = y if sm <= 10 else y - 1

w = int(d + (2.6 * sm - 0.2) + y + y // 4  + c // 4 - 2 * c ) % 7
print(f'{d}-{m}-{Y} is on -> {w}', end='')
print('Another statement here')
