a, b, c = 10, 20, 30
print(f'1. a: {a}  b: {b}  c: {c}')

*a, b, c = 10, 20, 30, 40, 50, 60
print(f'2. a: {a}  b: {b}  c: {c}')

a, *b, c = 10, 20, 30, 40, 50, 60
print(f'3. a: {a}  b: {b}  c: {c}')

a, b, *c = 10, 20, 30, 40, 50, 60
print(f'4. a: {a}  b: {b}  c: {c}')

a, b, *c = 10, 20
print(f'5. a: {a}  b: {b}  c: {c}')
